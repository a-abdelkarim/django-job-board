from django.shortcuts import render
from .models import Job


def job_list(request):
    job_list = Job.objects.all()
    context = {
        'jobs': job_list
    }

    return render(request, 'job/jobs.html', context)


def job_detail(request, id):
    job = Job.objects.get(id=id)
    context = {
        'job':job
    }

    return render(request, 'job/job_details.html', context)