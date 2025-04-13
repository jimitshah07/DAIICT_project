from django.shortcuts import render, redirect

def initial_questions_view(request):
    if request.method == 'POST':
        request.session['experience'] = request.POST.get('experience')
        request.session['tech_stack'] = request.POST.get('tech_stack')
        request.session['passion'] = request.POST.get('passion')
        return redirect('ai_questions')
    return render(request, 'career/questions.html')
