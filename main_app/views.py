import os
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Skill, Equipment
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
  id_list = skill.equipments.all().values_list('id')
  equipments_skill_doesnt_have = Equipment.objects.exclude(id__in=id_list)
  training_form = TrainingForm()
  return render(request, 'skills/detail.html', {'skill': skill, 'training_form': training_form, 'equipments': equipments_skill_doesnt_have})

class SkillCreate(CreateView):
  model = Skill
  fields = ['name', 'style', 'description', 'years']

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
   
class EquipmentList(ListView):
  model = Equipment

class EquipmentDetail(DetailView):
  model = Equipment

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentUpdate(UpdateView):
  model = Equipment
  fields = ['name', 'description']

class EquipmentDelete(DeleteView):
  model = Equipment
  success_url = '/equipments'

def assoc_equipment(request, skill_id, equipment_id):
  Skill.objects.get(id=skill_id).equipment.add(equipment_id)
  return redirect('detail', skill_id=skill_id)

def unassoc_equipment(request, skill_id, equipment_id):
  Skill.objects.get(id=skill_id).equipments.remove(equipment_id)
  return redirect('detail', skill_id=skill_id)