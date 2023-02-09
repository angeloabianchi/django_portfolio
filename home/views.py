from django.shortcuts import render


def index(request):
    response = render(request, 'home/index.html')
    return response