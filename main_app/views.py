from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Skill
from .forms import TrainingForm

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
    training_form = TrainingForm()
    return render(request, 'skills/detail.html', {
        'skill': skill, 'training_form': training_form
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

def add_training(request, skill_id):
   form = TrainingForm(request.POST)
   if form.is_valid():
        new_training = form.save(commit=False)
        new_training.skill_id = skill_id
        new_training.save()
        return redirect('detail', skill_id=skill_id)