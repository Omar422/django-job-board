from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
# import my form
from .form import ApplyJob, AddJob
from django.urls import reverse

# Create your views here.

def job_list(request):

    job_list = Job.objects.all()
    paginator = Paginator(job_list, 3) # Show n jobs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # must be a dict
    # context = {'name to use in template': name here}
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)
    

def job_detail(request, title_slug):
    
    job_detail = Job.objects.get(slug=title_slug) #.filter

    if request.method == 'POST':
        apply_form = ApplyJob(request.POST, request.FILES)
        if apply_form.is_valid():
            form = apply_form.save(commit=False)
            form.job = job_detail
            form.save()
    else:
        apply_form = ApplyJob()

    context = {'job': job_detail, 'apply_form': apply_form}
    return render(request, 'job/job_detail.html', context)

def add_job(request):
    
    if request.method == 'POST':
        add_form = AddJob(request.POST, request.FILES)
        if add_form.is_valid():
            # save without commit to db to add user id later
            form = add_form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        add_form = AddJob()

    return render(request, 'job/add_job.html', {'add_form': add_form})