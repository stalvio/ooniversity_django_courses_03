from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django import forms
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):

	try:
		course_detail = Course.objects.get(id = request.GET['course_id'])
		students = course_detail.student_set.all()
		i = 1
		for student in students:
			student.course_id = i
			student.courses_list = Course.objects.filter(student = student)
			i += 1
	except:
		course_detail = 0
		students = Student.objects.all()
		i = 1
		for student in students:
			student.course_id = i
			student.courses_list = Course.objects.filter(student = student)
			i += 1
	return render(request, 'students/list.html', {'students': students, 'course_detail': course_detail})

def detail(request, pk):
	student_detail = Student.objects.get(id = pk)
	student_detail.course_id = Course.objects.filter(student = student_detail)
	return render(request, 'students/detail.html',{'student_detail': student_detail})

def create(request):	
	if request.method == "POST":	
		form = StudentModelForm(request.POST)
		if form.is_valid():
			new_student = form.save()
			messages.success(request, "Student %s %s has been successfully added." % (new_student.name, new_student.surname))
			return redirect("students:list_view")
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html',{'form': form})

def edit(request, pk):
	current_stud = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=current_stud)
		if form.is_valid():
			current_stud = form.save()
			messages.success(request, "Info on the student has been sucessfully changed.")
			return redirect("students:edit", pk)
	else:
		form = StudentModelForm(instance=current_stud)
	return render(request, 'students/edit.html',{'form': form})

def remove(request, pk):
	removen_stud = Student.objects.get(id=pk)
	if request.method == 'POST':
		removen_stud.delete()
		messages.success(request,"Info on %s %s has been sucessfully deleted." % (removen_stud.name, removen_stud.surname))
		return redirect("students:list_view")
	else:
		form = removen_stud
	return render(request, 'students/remove.html', {'form': form})
# Create your views here.
