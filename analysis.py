from django.shortcuts import render, redirect
from career.utils.analyser import analyze_profile

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
