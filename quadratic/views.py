# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import math
from forms import QuadraticForm

x1=x2= None
 
def quadratic_results(request):	
	value = {}
	if request.GET:
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form['a'].value()
			b = form['b'].value()
			c = form['c'].value()
		 
			d = get_diskriminant(a, b, c)			   	
			value['diskr'], value['Korn'] = d['diskr'], d['Korn']
			
	else:
		form = QuadraticForm()
	value['form'] = form	
	return render(request, 'quadratic/results.html', value)	

def get_diskriminant(a,b,c):
	a = float(a)
	b = float(b)
	c = float(c)
	d = int((b ** 2) - (4 * a * c))
	d_ = {'diskr':'Дискриминант: %s \n'% d}
	if d == 0:
		x1 = round(float(- (b / ( 2 * a))))	
		d_['Korn'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x1
	elif d > 0:
		root = math.sqrt(d)
		x1 = round(float((-b + root) / (2 * a)))
		x2 = round(float((-b - root) / (2 * a)))
		d_['Korn'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s ' % (x1, x2)
	else:
		d_['Korn'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
	return d_
