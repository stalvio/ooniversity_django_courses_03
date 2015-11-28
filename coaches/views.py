from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, pk):
	coach_detail = Coach.objects.get(id = pk)
	coach_courses = Course.objects.filter(coach = coach_detail)
	assistant_courses =  Course.objects.filter(assistant = coach_detail)
	
	
	return render(request, 'coaches/detail.html', {'coach_detail': coach_detail, 'coach_courses': coach_courses, 'assistant_courses': assistant_courses})

# Create your views here.
