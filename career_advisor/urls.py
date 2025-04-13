# skill_assist/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advisor.urls')), 
    # path('accounts/', include('accounts.urls')),
]
