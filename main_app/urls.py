from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('skills/', views.skills_index, name="index"),
    path('skills/<int:skill_id>/', views.skills_detail, name='detail'),
]