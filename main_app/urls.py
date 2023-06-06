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
    path('skills/<int:skill_id>/add_training/', views.add_training, name='add_training'),
    path('skills/<int:skill_id>/assoc_equipment/<int:equipment_id>/', views.assoc_equipment, name='assoc_equipment'),
    path('skills/<int:skill_id>/unassoc_equipment/<int:equipment_id>/', views.unassoc_equipment, name='unassoc_equipment'),
    path('equipments/', views.EquipmentList.as_view(), name='equipments_index'),
    path('equipments/<int:pk>/', views.EquipmentDetail.as_view(), name='equipments_detail'),
    path('equipments/create/', views.EquipmentCreate.as_view(), name='equipments_create'),
    path('equipments/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipments_update'),
    path('equipments/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipments_delete'),
]