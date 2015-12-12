from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from feedbacks.models import Feedback

class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedback.html'
	context_object_name = "form"
	success_url = reverse_lazy('feedback')

	def form_valid(self, form):
		form.save()
		messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
		return super(FeedbackView, self).form_valid(form)

	


# Create your views here.
