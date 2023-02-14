from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    response = render(request, 'jobs/index.html', {'jobs':jobs})
    return response

def job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if job:
        response = render(request, 'jobs/job/job.html', {'job': job})
    else:
        response = render(request, 'jobs/index.html')
    return response

