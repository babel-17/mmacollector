from django.db import models
from django.urls import reverse

# Create your models here.
class Skill(models.Model):
   name = models.CharField(max_length=100) 
   style = models.CharField(max_length=100)
   description = models.TextField(max_length=250)
   years = models.IntegerField()

   def __str__(self):
      return f'{self.name} ({self.id})'

   def get_absolute_url(self):
      return reverse('detail', kwargs={'skill_id': self.id})
