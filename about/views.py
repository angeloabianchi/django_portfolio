from django.shortcuts import render


def index(request):
    response = render(request, 'about/index.html')
    return response