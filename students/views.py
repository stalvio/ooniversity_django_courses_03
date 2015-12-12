from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django import forms
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			students = Student.objects.filter(courses__id=course_id)
			for student in students:
				student.courses_list = Course.objects.filter(student = student)
		else:
			students = Student.objects.all()
			for student in students:
				student.courses_list = Course.objects.filter(student = student)
		return students
	
		

#def list_view(request):

	#try:
		#course_detail = Course.objects.get(id = request.GET['course_id'])
		#students = course_detail.student_set.all()
		#i = 1
		#for student in students:
		#	student.course_id = i
		#	student.courses_list = Course.objects.filter(student = student)
		#	i += 1
	#except:
		#course_detail = 0
		#students = Student.objects.all()
		#i = 1
		#for student in students:
		#	student.course_id = i
		#	student.courses_list = Course.objects.filter(student = student)
		#	i += 1
	#return render(request, 'students/list.html', {'students': students, 'course_detail': course_detail})

class StudentDetailView(DetailView):
	model = Student


	
#def detail(request, pk):
	#student_detail = Student.objects.get(id = pk)
	#student_detail.course_id = Course.objects.filter(student = student_detail)
	#return render(request, 'students/detail.html',{'student_detail': student_detail})

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	
	
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Student registration'
		return context
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, "Student %s %s has been successfully added." % (self.object.name, self.object.surname))
		return super(StudentCreateView, self).form_valid(form)

#def create(request):	
#	if request.method == "POST":	
#		form = StudentModelForm(request.POST)
#		if form.is_valid():
#			new_student = form.save()
#			messages.success(request, "Student %s %s has been successfully added." % (new_student.name, new_student.surname))
#			return redirect("students:list_view")
#	else:
#		form = StudentModelForm()
#	return render(request, 'students/add.html',{'form': form})

class StudentUpdateView(UpdateView):
	model = Student
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Student info update'
		return context

	def form_valid(self, form):
		messages.success(self.request, 'Info on the student has been sucessfully changed.')
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		return context

	def delete(self, request, *args, **kwargs):
		message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
		messages.success(self.request, 'Info on {} {} has been sucessfully deleted.' .format(self.object.name, self.object.surname))
		return message	

#def edit(request, pk):
#	current_stud = Student.objects.get(id=pk)

#	if request.method == 'POST':
#		form = StudentModelForm(request.POST, instance=current_stud)
#		if form.is_valid():
#			current_stud = form.save()
#			messages.success(request, "Info on the student has been sucessfully changed.")
#			return redirect("students:edit", pk)
#	else:
#		form = StudentModelForm(instance=current_stud)
#	return render(request, 'students/edit.html',{'form': form})

'''
def remove(request, pk):
	removen_stud = Student.objects.get(id=pk)
	if request.method == 'POST':
		removen_stud.delete()
		messages.success(request,"Info on %s %s has been sucessfully deleted." % (removen_stud.name, removen_stud.surname))
		return redirect("students:list_view")
	else:
		form = removen_stud
	return render(request, 'students/remove.html', {'form': form}) '''
# Create your views here.
