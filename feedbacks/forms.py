from django.shortcuts import render
from django.http import HttpResponse
from feedbacks.models import Feedback
from django import forms

class  FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'

