from django.http import HttpResponse


def test_student(request):
    return HttpResponse('<h1>Welcome to Student Django App</h1>')