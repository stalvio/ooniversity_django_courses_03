from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, pk):
	course_detail = Course.objects.get(id = pk)
	print course_detail
	lessons = course_detail.lesson_set.all()
	return render(request, 'courses/detail.html', { 'course_detail': course_detail , 'lessons': lessons, 'course_num' : pk})

# Create your views here.
