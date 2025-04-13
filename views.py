from django.shortcuts import render,redirect
from .ai_model import recommend_jobs
from .utils.ai_engine import generate_followup_questions
from .utils.analyser import analyze_profile
import google.generativeai as genai
from django.shortcuts import render
import os
from dotenv import load_dotenv
from django.http import HttpResponse
import re



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def find(request):
    results = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        results = recommend_jobs(user_input)
    return render(request, 'find_your_passion.html', {'results': results})


# Step 1: Landing Page
def landing_view(request):
    return render(request, 'career/landing.html')


# Step 2: User fills out initial info (experience, tech, passion)
def initial_questions_view(request):
    if request.method == 'POST':
        request.session['experience'] = request.POST.get('experience')
        request.session['tech_stack'] = request.POST.get('tech_stack')
        request.session['passion'] = request.POST.get('passion')
        return redirect('ai_questions')
    return render(request, 'career/questions.html')


# Step 3: Show 3 AI-generated questions based on initial answers
def ai_questions_view(request):
    if request.method == 'POST':
        answers = [request.POST.get(f'q{i}') for i in range(1, 4)]
        request.session['ai_answers'] = answers
        return redirect('analysis')

    experience = request.session.get('experience', '')
    tech_stack = request.session.get('tech_stack', '')
    passion = request.session.get('passion', '')

    questions = generate_followup_questions(experience, tech_stack, passion)
    return render(request, 'career/ai_questions.html', {'questions': questions})


def analysis_view(request):
    if not request.session.get('ai_answers'):
        return redirect('landing')

    data = {
        'experience': request.session.get('experience'),
        'tech_stack': request.session.get('tech_stack'),
        'passion': request.session.get('passion'),
        'ai_answers': request.session.get('ai_answers'),
    }

    analysis = analyze_profile(data)
    request.session['analysis'] = analysis
    return render(request, 'career/analysis.html', {'analysis': analysis})


# Step 5: Show final roadmap
def roadmap_view(request):
    roadmap = request.session.get('analysis', {}).get('roadmap', [])
    return render(request, 'career/roadmap.html', {'roadmap': roadmap})



# views.py
import requests
from django.http import JsonResponse

# LinkedIn API credentials (replace these with your actual credentials)
API_KEY = "78gykyu7adgkek"  # Your LinkedIn API key
API_SECRET = "WPL_AP1.pfCEAJczkpZdn5Vi.G+95rA=="  # Your LinkedIn API secret
ACCESS_TOKEN = "2 months"  # OAuth access token

# Function to fetch profiles from LinkedIn API
def fetch_linkedin_profiles(request):
    # LinkedIn API endpoint for job titles or simple profile searches
    url = "https://api.linkedin.com/v2/search?q=jobs&keywords=data%20scientist"

    # Set up headers for OAuth token authentication
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }

    # Send a request to LinkedIn API
    response = requests.get(url, headers=headers)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        profiles = response.json()
        # Return the profiles as a JSON response (can be processed further in frontend)
        return JsonResponse(profiles, safe=False)
    else:
        # Handle API request errors
        return JsonResponse({'error': 'Error fetching data from LinkedIn API', 'status_code': response.status_code}, status=500)


def display_linkedin_profiles(request):
    return render(request, 'career/linkedin_profiles.html')



genai.configure(api_key="AIzaSyCkRX0dGN_dfUkyUjhpvrXB1gFpkNTJJA4")

def select_career(request):
    return render(request, 'career/select_career.html')

def show_professionals(request):
    career = request.GET.get('career', 'Data Science')

    # Prompt to Gemini for multiple professionals
    prompt = f"Give me three real, well-known people associated with the field of {career}. Return their full name and their public LinkedIn profile URL if available. Format the output as: Name: [Full Name]\nLinkedIn: [LinkedIn URL] (if available)."

    professionals = []
    ai_summary = "No information found."

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Or your preferred model
        response = model.generate_content(prompt)
        ai_summary = response.text

        # Use regular expressions to extract names and LinkedIn URLs
        name_matches = re.findall(r"Name:\s*(.+)", ai_summary)
        linkedin_matches = re.findall(r"LinkedIn:\s*(https?://www\.linkedin\.com/in/[a-zA-Z0-9_-]+/?)(.*)", ai_summary)

        num_results = len(name_matches)
        for i in range(num_results):
            name = name_matches[i].strip()
            linkedin = "#"  # Default if no LinkedIn found for this person

            # Try to find a corresponding LinkedIn link
            for link_match in linkedin_matches:
                if name.lower() in link_match[0].lower():  # Basic association by name in URL
                    linkedin = link_match[0].strip()
                    break
                elif i < len(linkedin_matches): # Fallback if direct association fails and there are more links
                    linkedin = linkedin_matches[i][0].strip()
                    break

            professionals.append({
                'name': name,
                'linkedin': linkedin if linkedin != "#" else f"https://www.linkedin.com/search/results/people/?keywords={name.replace(' ', '%20')}"
            })

        # Ensure we have at least 3 entries, with a generic search if Gemini didn't provide enough
        while len(professionals) < 3:
            professionals.append({
                'name': "Could Not Find Specific Person",
                'linkedin': f"https://www.linkedin.com/search/results/people/?keywords={career.replace(' ', '%20')}"
            })

        return render(request, "career/show_professionals.html", {
            "career": career,
            "ai_summary": ai_summary,
            "professionals": professionals
        })

    except Exception as e:
        error_message = f"<h2>Error: {str(e)}</h2><p>Check if your Gemini API key is valid.</p>"
        return HttpResponse(error_message)