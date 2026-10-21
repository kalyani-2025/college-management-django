from django.http import HttpResponse


def faculty_home(request):
    return HttpResponse("<h1>Welcome to Faculty Home Page</h1>")


def faculty_profile(request):
    return HttpResponse("Welcome to Faculty Profile Page")
