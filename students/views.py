from django.http import HttpResponse


def student_home(request):
    return HttpResponse("<h1>Welcome to Student Home Page</h1>")


def student_profile(request):
    return HttpResponse("Welcome to Student Profile Page")


def student_courses(request):
    return HttpResponse("Welcome to Student Courses Page")
