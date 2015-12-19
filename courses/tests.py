# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.test import Client
from django.contrib.auth.models import User
	
def new_courses():

		test_user1 = User.objects.create(
										username = 'user1')	
		test_user2 = User.objects.create(
										username = 'user2')
		test_user3 = User.objects.create(
										username = 'user3')	
		
		test_coach_1 = Coach.objects.create(
											User = test_user1,	
											date_of_birth = "0101-01-01",
											gender = "M",
											phone = "010101",
											address = "Kharkov 1",
											skype = "coach_1",
											description = "Greate coach #1"
											)
		test_coach_2 = Coach.objects.create(
											User = test_user2,	
											date_of_birth = "0202-02-02",
											gender = "M",
											phone = "020202",
											address = "Kharkov 2",
											skype = "coach_2",
											description = "Greate coach #2"
											)
		test_coach_3 = Coach.objects.create(
											User = test_user3,	
											date_of_birth = "0303-03-03",
											gender = "F",
											phone = "030303",
											address = "Kharkov 3",
											skype = "coach_3",
											description = "Greate coach #3"
											)
		
		course_1 = Course.objects.create(
					name="PYTHON",
					short_description = "4-х недельный курс онлайн изучения языка Python",
					description = "Hello! Курс является введением в язык программирования Python.",
					coach = test_coach_1,
					assistant = test_coach_2)
	
		course_2 = Course.objects.create(
					name="Django",
					short_description = "6-х недельный курс онлайн изучения языка Python",
					description = "Django курс всё разъясняет очень подробно. ",
					coach = test_coach_2,
					assistant = test_coach_3)
	
		course_3 = Course.objects.create(
					name="HTML и  CSS",
					short_description = "Курс верстки сайта на языке HTML и CSS",
					description = "Начальный путь обучения будущих веб-мастеров должен начинаться с курса по изучению HTML и CSS",	
					coach = test_coach_3,
					assistant = test_coach_1)

class CoursesListTest(TestCase):
	
	def test_course_open_page(self):
		client = Client()
		response = client.get("/")
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_add_course(self):
		client = Client()
		response = client.get("/courses/add/")
		self.assertTemplateUsed(response, 'courses/add.html')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Name")
		self.assertContains(response, "Short description")
		self.assertContains(response, "Coach")
		self.assertContains(response, "Assistant")
	
	
# Create your tests here.
