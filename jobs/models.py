from django.db import models

JOB_TYPE_CHOICES = [
    ('FullTime', 'Full Time'),
    ('PartTime', 'Part Time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
]

class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    description = models.TextField()
    requirements = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"
