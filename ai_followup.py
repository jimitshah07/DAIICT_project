from django.shortcuts import render, redirect
from career.utils.ai_engine import generate_followup_questions

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
