from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Skill, JobProfile, UserSkillAssessment, UserSkillProficiency, UserAssessment
from .forms import AssessmentForm
from transformers import pipeline

# Home view: Render the home page, only accessible to logged-in users
@login_required
def home(request):
    return render(request, 'home.html')

# Skill assessment view: Handles both GET (to show skills) and POST (to process the assessment)
@login_required
def skill_assessment(request):
    skills = Skill.objects.all()  # Get all skills from the database
    if request.method == 'POST':
        user_name = request.POST['user_name']  # Get the user's name from the form
        user_assessment = UserSkillAssessment.objects.create(user_name=user_name)  # Create a new assessment record
        
        for skill in skills:
            proficiency = request.POST.get(skill.name)  # Get proficiency level for each skill
            if proficiency:
                # Save the skill proficiency to the UserSkillProficiency model
                UserSkillProficiency.objects.create(
                    user=user_assessment,
                    skill=skill,
                    proficiency=proficiency
                )
        
        # After saving the skill assessment, redirect to start_assessment page
        return redirect('start_assessment')  # This redirects to the start_assessment page

    # If GET request, render the form with all skills
    return render(request, 'skill_assessment.html', {'skills': skills})  # Change 'start-assessment.html' to 'skill_assessment.html'
# Recommend jobs based on the user's skill assessment
def recommend_jobs(request, user_assessment_id):
    user_assessment = UserSkillAssessment.objects.get(id=user_assessment_id)  # Get the user assessment
    user_skills = UserSkillProficiency.objects.filter(user=user_assessment)  # Get the user's skills and proficiencies

    recommended_jobs = []  # List to hold recommended jobs
    for job in JobProfile.objects.all():
        job_skills = job.required_skills.all()  # Get the skills required for the job
        matching_skills = job_skills.filter(id__in=[skill.skill.id for skill in user_skills])  # Check if the user has the required skills

        if matching_skills:  # If there are matching skills, add the job to the recommended jobs list
            recommended_jobs.append({
                'job_title': job.title,
                'matching_skills': [skill.name for skill in matching_skills]
            })

    return JsonResponse({"recommended_jobs": recommended_jobs})  # Return the recommended jobs in a JSON response

# Function to generate career-related questions based on the user's interests (AI in this case)
from transformers import pipeline

def generate_questions(interests):
    # Initialize the text-generation pipeline with GPT-2 or GPT-3 model
    generator = pipeline("text-generation", model="gpt2")

    # Define the prompt for career-related questions
    prompt = f"Generate 5 insightful career-related questions for someone interested in {interests}.<br>"
    prompt += "The questions should focus on skills required, industry applications, future trends, learning resources, and ethical considerations.<br>"
    prompt += "Each question should challenge the person to think critically about AI's impact and their role in it.<br>"

    # Generate the questions using the model
    result = generator(prompt, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2, num_beams=5)

    # Extract the generated text
    generated_text = result[0]['generated_text']

    # Split the output by the '?' symbol, as each question ends with a question mark
    questions = [q.strip() for q in generated_text.split('?') if q.strip()]

    # Re-adding the '?' at the end of each question
    questions = [q + '?' for q in questions]

    # Return the questions as an HTML formatted string with <br> line breaks
    formatted_questions = '<br>'.join(questions)
    
    return formatted_questions


# View to start the assessment (form submission to generate career-related questions)
@login_required
def start_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)  # Create a form instance with the POST data
        if form.is_valid():  # Check if the form is valid
            user_type = form.cleaned_data['user_type']  # Get the user's type
            interests = form.cleaned_data['interests']  # Get the user's interests
            questions = generate_questions(interests)  # Generate questions based on the user's interests

            # Create a UserAssessment object with the generated questions
            assessment = UserAssessment.objects.create(
                user=request.user,
                user_type=user_type,
                interests=interests,
                generated_questions=questions
            )
            # Redirect to the 'show_test' view to display the generated questions
            return redirect('show_test', assessment_id=assessment.id)
    else:
        form = AssessmentForm()  # If GET request, show the empty form

    return render(request, 'advisor/start_assessment.html', {'form': form})  # Render the form for the user to fill

# View to show the test (display the generated questions)
@login_required
def show_test(request, assessment_id):
    assessment = UserAssessment.objects.get(id=assessment_id, user=request.user)  # Get the user's assessment record
    return render(request, 'advisor/show_test.html', {'assessment': assessment})  # Render the test page with the assessment data

# Job market data (hardcoded for now, can be extended in the future)
job_market_data = {
    "Software Engineer": {"demand": 5, "average_salary": 100000},
    "Data Scientist": {"demand": 4, "average_salary": 120000},
    "Product Manager": {"demand": 3, "average_salary": 110000},
}
