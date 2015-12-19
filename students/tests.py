# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course
from students.models import Student
from django.test import Client



def new_objects_test():
	
	course_1 = Course.objects.create(
					name="PYTHON",
					short_description = "4-х недельный курс онлайн изучения языка Python",
					description = "Hello! Курс является введением в язык программирования Python.")
	
	course_2 = Course.objects.create(
					name="Django",
					short_description = "6-х недельный курс онлайн изучения языка Python",
					description = "Django курс всё разъясняет очень подробно. ")
	
	course_3 = Course.objects.create(
					name="HTML и  CSS",
					short_description = "Курс верстки сайта на языке HTML и CSS",
					description = "Начальный путь обучения будущих веб-мастеров должен начинаться с курса по изучению HTML и CSS")	
	student_1 = Student.objects.create(
							name='Kevin',
                            surname='Levrone',
                            date_of_birth='1966-07-16',
                            email='levrony@gmail.com',
                            phone='00220011',
                            address='USA, Baltimor',
                            skype='kevLevr')
	student_1.courses.add(course_1)

	student_2 = Student.objects.create(
							name='Werner',
                            surname='Shlager',
                            date_of_birth='1972-10-12',
                            email='Werner@inbox.ru',
                            phone='0505050505',
                            address='Austria',
                            skype='Werner')
	student_2.courses.add(course_2)

	student_3 = Student.objects.create(
							name='Migel',
                            surname='Levrone',
                            date_of_birth='1980-10-29',
                            email='Cotto@gmail.com',
                            phone='07070707',
                            address='Puerto-Rico',
                            skype='Cotto_Migel')	
	student_3.courses.add(course_3)

class StudentsListTest(TestCase):
	
	

	def test_course_list(self):
		new_objects_test()
		client = Client()
		response = client.get("/students/")
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_list.html')
		self.assertContains(response, "Kevin")
		self.assertContains(response, "skype")
		self.assertContains(response, "курсы")
		self.assertContains(response, "фамилия имя")
		self.assertContains(response, "USA")

	def test_count_students(self):
		new_objects_test()
		self.assertEqual(Student.objects.all().count(), 3)
	
	def test_add_student(self):
		client = Client()
		response = self.client.get("/students/add/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Name")
		self.assertContains(response, "Date of birth")
		self.assertContains(response, "Address")
		self.assertContains(response, "Surname")
		self.assertContains(response, "Phone")
		self.assertContains(response, "Courses")
		self.assertContains(response, "Skype")
		self.assertContains(response, "Student registration")
	
	def test_edit_student(self):
		new_objects_test()
		client = Client()
		response = self.client.get("/students/edit/1/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Kevin')
		self.assertContains(response, 'Levrone')
		self.assertContains(response, "PYTHON")
	
	def test_delete_student(self):
		new_objects_test()
		client = Client()
		response = self.client.get("/students/remove/1/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Student info suppression')

class StudentsDetailTest(TestCase):
	
	def test_detail_page(self):
		new_objects_test()
		client = Client()
		response = self.client.get('/students/2/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_detail.html')
	
	def test_address_detail(self):
		new_objects_test()
		client = Client()
		response = self.client.get('/students/2/')
		self.assertContains(response, 'Austria')	
	
	def test_skype_detail(self):
		new_objects_test()
		client = Client()
		response = self.client.get('/students/2/')
		self.assertContains(response, 'Werner')

	def test_mail_detail(self):
		new_objects_test()
		client = Client()
		response = self.client.get('/students/2/')
		self.assertContains(response, 'Werner@inbox.ru')

	def test_course(self):
		new_objects_test()
		client = Client()
		response = self.client.get('/students/2/')
		self.assertContains(response, "Django")
	

# Create your tests here.
