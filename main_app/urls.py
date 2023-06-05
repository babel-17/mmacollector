from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('skills/', views.skills_index, name="index"),
    path('skills/<int:skill_id>/', views.skills_detail, name='detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),
]