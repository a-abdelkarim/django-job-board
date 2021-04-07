from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job
from .forms import ApplyForm, JobForm


def job_list(request):
    job_list = Job.objects.all()

    #--> Paginator
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'job_list': job_list
    }

    return render(request, 'job/jobs.html', context)


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)

    # Apply Form
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()

    else:
        form = ApplyForm()
    # End Apply Form


    context = {
        'job':job,
        'form':form
    }

    return render(request, 'job/job_details.html', context)



def add_job(request):
    
    context = {
        'form':JobForm
    }
    return render(request, 'job/add_job.html', context)