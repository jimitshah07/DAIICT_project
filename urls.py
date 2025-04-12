from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('assessment/', views.assessment, name='assessment'),
    path('results/<str:skills>/', views.results, name='results'),
    path('resume/', views.resume, name='resume'),
    path('', views.home, name='home'),
    path('skill-assessment/', views.skill_assessment, name='skill_assessment_start'),
    path('job-market/', views.job_market_view, name='job_market'),
]
