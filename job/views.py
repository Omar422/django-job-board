from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):

    job_list = Job.objects.all()
    # must be a dict
    # context = {'name to use in template': name here}
    context = {'jobs': job_list}
    return render(request, 'job/job_list.html', context)
    

def job_detail(request, job_id):
    
    job_detail = Job.objects.get(id=job_id) #.filter
    context = {'job': job_detail}
    return render(request, 'job/job_detail.html', context)