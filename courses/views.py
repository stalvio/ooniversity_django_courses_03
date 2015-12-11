from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django import forms
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
	model = Course
	template_name = "courses/detail.html"
	context_object_name = "course_detail"


'''
def detail(request, pk):
	course_detail = Course.objects.get(id = pk)
	lessons = course_detail.lesson_set.all()

	return render(request, 'courses/detail.html', { 'course_detail': course_detail , 'lessons': lessons, 'course_num' : pk})
'''

class CourseCreateView(CreateView):
	model = Course
	template_name = "courses/add.html"
	context_object_name = "form"
	success_url = reverse_lazy('index')
	
	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Course creation'
		return context

	def form_valid(self, form):
		form.save()
		messages.success(self.request, "Course %s has been successfully added." % (form.instance.name))
		return super(CourseCreateView, self).form_valid(form)

'''
def add(request):	
	if request.method == "POST":	
		form = CourseModelForm(request.POST)
		if form.is_valid():
			new_course = form.save()
			messages.success(request, "Course %s has been successfully added." % (new_course.name))
			return redirect("index")
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html',{'form': form})
'''
class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'

	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Course update"
		return context

	def get_success_url(self):
		return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

	
	def form_valid(self, form):
		message = super(CourseUpdateView, self).form_valid(form)
		messages.success(self.request, 'The changes have been saved.')
		return message

'''
def edit(request, pk):
	current_course = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=current_course)
		if form.is_valid():
			current_course = form.save()
			messages.success(request, "The changes have been saved.")
			return redirect("courses:edit", pk)
	else:
		form = CourseModelForm(instance=current_course)
	return render(request, 'courses/edit.html',{'form': form})
'''
class CourseDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('index')
	template_name = "courses/remove.html"
	context_object_name = 'form'

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Course deletion"
		return context

	def delete(self, request, **kwargs):
		message = super(CourseDeleteView, self).delete(request, **kwargs)
		messages.success(self.request, "Course %s has been deleted." % (self.object.name))
		return message	

'''
def remove(request, pk):
	removen_course = Course.objects.get(id=pk)
	if request.method == 'POST':
		removen_course.delete()
		messages.success(request,"Course %s has been deleted." % (removen_course.name))
		return redirect("index")
	else:
		form = removen_course
	return render(request, 'courses/remove.html', {'form': form})
'''

class LessonCreateView(CreateView):
	model = Lesson
	template_name = "courses/add_lesson.html"
	context_object_name = "form"
	#success_url = reverse_lazy('courses:detail')

	def get_context_data(self, **kwargs):
		context = super(LessonCreateView, self).get_context_data(**kwargs)
		context['title'] = "Lesson create"
		return context

	def get_success_url(self):
		print self.object.pk
		return reverse_lazy('courses:detail',  kwargs={'pk': self.object.course_id})
	
	def form_valid(self, form):
		message = super(LessonCreateView, self).form_valid(form)
		messages.success(self.request, "Lesson %s has been successfully added." % (self.object.subject))
		return message

'''
def add_lesson(request, pk):

	current_course = Course.objects.get(id=pk)
	if request.method == "POST":	
		form = LessonModelForm(request.POST)
		if form.is_valid():
			new_lesson = form.save()
			messages.success(request, "Lesson %s has been successfully added." % (new_lesson.subject))
			return redirect("courses:detail", pk)
	else:
		form = LessonModelForm(initial={'course' : pk})
	return render(request, 'courses/add_lesson.html',{'form': form})
'''
# Create your views here.
