from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home),
    path('profile/', views.student_profile),
    path('courses/', views.student_courses),
]
