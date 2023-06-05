from django.shortcuts import render

skills = [
  {'name': 'BJJ', 'style': 'grappling', 'description': 'submission', 'years': 5},
  {'name': 'Boxing', 'style': 'striking', 'description': 'force', 'years': 10},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills_index(request):
    return render(request, 'skills/index.html', {
        'skills': skills    
    })