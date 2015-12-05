from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from django import forms

class  CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'short_description', 'description', 'coach', 'assistant']

class  LessonModelForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ['subject', 'description', 'course', 'order' ]
