# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import TempReading, School
from .forms import Schools
from django.utils import timezone
import csv
from datetime import datetime

# Create your views here.
def index(request):
	logout(request)
	return render(request, 'temperatures/index.html')
	

def logged(request):
	user = request.POST.get('your_name')
	password = request.POST.get('your_pass')
	user = authenticate(request, username=user, password=password)
	if(user is not None):
		login(request, user)
		return redirect('welcome')
	else:
		return redirect('index')

def my_logout(request):
	logout(request)
	return redirect('index')

#Defines the welcome page where the user selects their school to view more details about
@login_required #checks if user is actually login()
@permission_required('temperatures.Can_view_temp_readings')
def welcome(request):

	print('test')
	form = Schools()
	return render(request, 'temperatures/welcome.html', {'form':form})

def gotodetail(request):
	choice = request.POST.get('schoolchoice') #Converted the school object to string for url formatting
	return redirect('school', school = choice)

def download_data(request):
	filter = request.POST.get('downloadoptions')
	data = filter_date(filter)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="filtered_data.csv"'
	
	#get from selection to determine how far to look back for data
	writer = csv.writer(response)
	for x in data:
		writer.writerow([x.date, x.temp, x.humidity, x.school])

	return response

#This view displays all the temperature readings of a particular school and 
@login_required
@permission_required('temperatures.Can_view_temp_readings')
def detail(request, school):
	url = 'schools/' + school + '/index.html'
	readings = TempReading.objects.filter(school=school)
	context = {'context': readings, 'name' : User.username, 'choice': school}
	return render(request, url, context)

#This view is used to filter queries on a schools detail page. AKA lets the user sort between readings from the past; this is a date in the format yyyy-mm-dd
@login_required
@permission_required('temperatures.Can_view_temp_readings')
def refreshdetail(request):
	filter = request.POST.get('filteroptions')
	if(type(filter)!= type(datetime)):
		redirect("refreshdetail.html")
	
	data = filter_date(filter)
	context = {'context': data, 'name' : User.username}
	return render(request, 'refreshdetail.html', context) 
	
def getschoolchoice(request):
	if(request.method == 'POST'):
		choice = request.POST.get('schoolchoice')
		return choice

def filter_date(filter_date):
	start_date = datetime.now()
	end_date = datetime.strptime(filter_date, "%Y-%m-%d")
	data = TempReading.objects.filter(date__lte=start_date, date__gte=end_date)
	return data