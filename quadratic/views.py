# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import math

x1=x2= None
 
def quadratic_results(request):	
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	value = {'a': a, 'b': b, 'c': c}
	error = {'er_a': '', 'er_b': '', 'er_c': ''}	
	flag = False			 
	for item in value.keys():
		if item == 'a' and value[item]== '0':
			error['er_a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'		
			flag = True
		elif value[item]== '':
			error['er_' + item] = 'коэффициент не определен'
			flag = True  
		else:				
			try:
				value[item] = int(value[item])
			except ValueError:
				error['er_' + item] = 'коэффициент не целое число'	
				flag = True
	
	for item in error.keys():
		value[item] = error[item]    

	if not flag:		
		di = diskr(value['a'], value['b'], value['c'])
		value['diskrim'], value['Korn']	= di['diskrim'], di['Korn']
	
	return render(request, 'results.html', value)	

def diskr(a,b,c):
	a = float(a)
	b = float(b)
	c = float(c)
	d = int((b ** 2) - (4 * a * c))
	d_ = {'diskrim':'Дискриминант: %s \n'% d}
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
