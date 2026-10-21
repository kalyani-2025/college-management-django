from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_home),
    path('profile/', views.faculty_profile),
]