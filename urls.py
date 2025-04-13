from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skill_assessment/', views.skill_assessment, name='skill_assessment'),
    path('recommend-jobs/<int:user_assessment_id>/', views.recommend_jobs, name='recommend_jobs'),
    path('start-assessment/', views.start_assessment, name='start_assessment'),
    path('test/<int:assessment_id>/', views.show_test, name='show_test'),
]
