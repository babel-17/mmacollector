from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Skill

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills_index(request):
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', {
        'skills': skills    
    })

def skills_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    return render(request, 'skills/detail.html', {
        'skill': skill
    })

class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'

class SkillUpdate(UpdateView):
    model = Skill
    fields = ['style', 'description', 'years']

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/skills'