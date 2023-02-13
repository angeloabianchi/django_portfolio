from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    response = render(request, 'jobs/index.html', {'jobs':jobs})
    return response

