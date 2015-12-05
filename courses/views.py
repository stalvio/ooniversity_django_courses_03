from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django import forms
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, pk):
	course_detail = Course.objects.get(id = pk)
	lessons = course_detail.lesson_set.all()
	#print course_detail.coach.id
	return render(request, 'courses/detail.html', { 'course_detail': course_detail , 'lessons': lessons, 'course_num' : pk})

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

def edit(request, pk):
	current_course = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=current_course)
		if form.is_valid():
			current_course = form.save()
			messages.success(request, "Info on the course has been sucessfully changed.")
			return redirect("courses:edit", pk)
	else:
		form = CourseModelForm(instance=current_course)
	return render(request, 'courses/edit.html',{'form': form})

def remove(request, pk):
	removen_course = Course.objects.get(id=pk)
	if request.method == 'POST':
		removen_course.delete()
		messages.success(request,"Info on %s has been sucessfully deleted." % (removen_course.name))
		return redirect("index")
	else:
		form = removen_course
	return render(request, 'courses/remove.html', {'form': form})

def add_lesson(request, pk):
	print 'hello'
	current_course = Course.objects.get(id=pk)
	if request.method == "POST":	
		form = LessonModelForm(request.POST)
		if form.is_valid():
			new_lesson = form.save()
			print new_lesson
			messages.success(request, "Lesson %s has been successfully added." % (new_lesson))
			return redirect("courses:detail", pk)
	else:
		form = LessonModelForm(initial={'course' : pk})
	return render(request, 'courses/add_lesson.html',{'form': form})

# Create your views here.
