from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'description', 'deadline',)
        widgets = {
            'deadline': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'style':'width:150px;', 'placeholder':'Select a date', 'type':'date'}),
        }