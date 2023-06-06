from django.db import models
from django.urls import reverse
from datetime import date

PARTS = (
   ('M', 'Morning'),
   ('N', 'Noon'),
   ('E', 'Evening'),
)

class Equipment(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(max_length=50)

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse('equipments_detail', kwargs={'pk': self.id})

# Create your models here.
class Skill(models.Model):
   name = models.CharField(max_length=100) 
   style = models.CharField(max_length=100)
   description = models.TextField(max_length=250)
   years = models.IntegerField()
   equipments = models.ManyToManyField(Equipment)

   def __str__(self):
      return f'{self.name} ({self.id})'

   def get_absolute_url(self):
      return reverse('detail', kwargs={'skill_id': self.id})
   
   def trained_for_today(self):
      return self.training_set.filter(date=date.today()).count() >= len(PARTS)

class Training(models.Model):
   date = models.DateField()
   part = models.CharField(
      max_length=1,
      choices=PARTS,
      default=PARTS[0][0]
   )
   skill = models.ForeignKey(
      Skill,
      on_delete=models.CASCADE
   )

   def __str__(self):
      return f"{self.get_part_display()} on {self.date}"
   
   class Meta:
      ordering = ['-date']