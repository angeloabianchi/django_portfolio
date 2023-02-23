from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    context = {'now': now}
    response = render(request, 'home/index.html', context)
    return response