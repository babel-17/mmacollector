from django.contrib import admin
from .models import Skill, Training, Equipment

# Register your models here.
admin.site.register(Skill)
admin.site.register(Training)
admin.site.register(Equipment)