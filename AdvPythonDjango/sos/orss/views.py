from django.http import HttpResponse


def test_orss(request):
    return HttpResponse("Hello, ORSS!")