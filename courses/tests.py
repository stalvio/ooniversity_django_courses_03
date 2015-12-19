from django.test import TestCase
from courses.models import Course
from django.test import Client

class CoursesListTest(TestCase):
	
	def test_course_list(self):
		client = Client()
		response = client.get("/")
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	
# Create your tests here.
