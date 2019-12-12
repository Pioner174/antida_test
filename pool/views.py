from django.http import HttpResponse


def index(request):
    return HttpResponse("Test django3.0 first project")