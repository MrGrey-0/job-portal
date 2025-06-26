from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()

    title = request.GET.get('title')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    if title:
        jobs = jobs.filter(title__icontains=title)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if salary_min:
        jobs = jobs.filter(salary_min__gte=salary_min)
    if salary_max:
        jobs = jobs.filter(salary_max__lte=salary_max)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_create.html', {'form': form})
