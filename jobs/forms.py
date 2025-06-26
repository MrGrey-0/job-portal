from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'p-2 border rounded w-full'}),
            'company_name': forms.TextInput(attrs={'class': 'p-2 border rounded w-full'}),
            'location': forms.TextInput(attrs={'class': 'p-2 border rounded w-full'}),
            'job_type': forms.Select(attrs={'class': 'p-2 border rounded w-full'}),
            'salary_min': forms.NumberInput(attrs={'class': 'p-2 border rounded w-full'}),
            'salary_max': forms.NumberInput(attrs={'class': 'p-2 border rounded w-full'}),
            'application_deadline': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'p-2 border rounded w-full'
            }),
            'description': forms.Textarea(attrs={'class': 'p-2 border rounded w-full'}),
            'requirements': forms.Textarea(attrs={'class': 'p-2 border rounded w-full'}),
            'responsibilities': forms.Textarea(attrs={'class': 'p-2 border rounded w-full'}),
        }
