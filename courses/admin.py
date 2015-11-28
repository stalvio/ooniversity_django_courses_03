from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
	model = Lesson
	list_display = ['subject', 'description', 'order']	
	extra = 0

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	fields = ['name', 'short_description', 'description']
	inlines = [LessonInline]
	search_fields = ['name']	


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
