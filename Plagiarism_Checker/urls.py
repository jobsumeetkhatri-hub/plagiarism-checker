"""Plagiarism_Checker URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plagiarismchecker.urls')),  # Fixed: now points to urls.py (plural)
]
