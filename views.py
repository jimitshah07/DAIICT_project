from django.shortcuts import render,redirect
from .ai_model import recommend_jobs
from .utils.ai_engine import generate_followup_questions
from .utils.analyser import analyze_profile

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


# Step 4: Analyze user profile based on all responses
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
