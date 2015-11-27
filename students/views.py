from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student

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
	print students
	return render(request, 'students/list.html', {'students': students, 'course_detail': course_detail})

def detail(request, pk):
	student_detail = Student.objects.get(id = pk)
	student_detail.course_id = Course.objects.filter(student = student_detail)
	return render(request, 'students/detail.html',{'student_detail': student_detail})
# Create your views here.
