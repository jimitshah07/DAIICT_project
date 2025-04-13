from django.shortcuts import render

def roadmap_view(request):
    roadmap = request.session.get('analysis', {}).get('roadmap', [])
    return render(request, 'career/roadmap.html', {'roadmap': roadmap})
