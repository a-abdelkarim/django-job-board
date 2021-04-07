from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job


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
    context = {
        'job':job
    }

    return render(request, 'job/job_details.html', context)