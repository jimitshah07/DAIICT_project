from django.shortcuts import render
import json
# Create your views here.
# Sample data for job market analysis
job_market_data = {
    "Software Engineer": {"demand": 5, "average_salary": 100000},
    "Data Scientist": {"demand": 4, "average_salary": 120000},
    "Product Manager": {"demand": 3, "average_salary": 110000},
}

def index(request):
    return render(request, 'index.html')

# def home(request):
#     return render(request, 'home.html')

def job_market_view(request):
    # Example data (you can fetch from DB or API instead)
    job_titles = ['Data Scientist', 'Web Developer', 'AI Engineer', 'Cloud Architect', 'DevOps Engineer']
    demand_scores = [85, 70, 90, 65, 75]

    context = {
        'job_titles': job_titles,
        'demand_scores': demand_scores
    }
    return render(request, 'job_market.html', context)

def job_market_analysis(request):
    job_titles = ["Software Engineer", "Data Analyst", "Digital Marketer", "Cybersecurity Expert", "UI/UX Designer"]
    demand_scores = [85, 75, 65, 90, 70]

    # jobs = [
    #     {"title": "Software Engineer", "description": "Build and maintain software solutions.", "image_url": "/static/images/software.jpg"},
    #     {"title": "Data Analyst", "description": "Analyze and interpret complex data.", "image_url": "/static/images/data.jpg"},
    #     {"title": "Cybersecurity Expert", "description": "Protect systems from cyber threats.", "image_url": "/static/images/cybersecurity.jpg"},
    #     {"title": "UI/UX Designer", "description": "Design user-friendly interfaces.", "image_url": "/static/images/uiux.jpg"},
    # ]

    # return render(request, 'job_market.html', {
    #     'job_titles': json.dumps(job_titles),
    #     'demand_scores': json.dumps(demand_scores),
    #     'jobs': jobs,
    # })
    
def skill_assessment(request):
    if request.method == 'POST':
        form = SkillAssessmentForm(request.POST)
        if form.is_valid():
            # process data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            skills = form.cleaned_data['skills']
            return render(request, 'assessment_result.html', {'name': name, 'skills': skills})
    else:
        form = SkillAssessmentForm()
    return render(request, 'skill_assessment.html', {'form': form})

def assessment(request):
    if request.method == 'POST':
        skills = request.POST.getlist('skills')
        return redirect('results', skills=json.dumps(skills))
    return render(request, 'assessment.html')

def results(request, skills):
    skills = json.loads(skills)
    recommendations = {skill: job_market_data.get(skill, {}) for skill in skills}
    return render(request, 'results.html', {'recommendations': recommendations})

def resume(request):
    return render(request, 'resume.html')