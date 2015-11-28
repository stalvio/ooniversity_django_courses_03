from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


def detail(request, pk):
	course_detail = Course.objects.get(id = pk)
	lessons = course_detail.lesson_set.all()
	#print course_detail.coach.id
	return render(request, 'courses/detail.html', { 'course_detail': course_detail , 'lessons': lessons, 'course_num' : pk})

# Create your views here.
