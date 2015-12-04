from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from django import forms

class  StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
		
