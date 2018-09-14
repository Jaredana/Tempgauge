# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TempReading, School
from .forms import Schools
from django.utils import timezone
import datetime
# Create your views here.
def index(request):
	alltemps = TempReading.objects.all()
	context = {'context': alltemps}
	return render(request, 'temperatures/index.html', context)

#Defines the welcome page where the user selects their school to view more details about
def welcome(request):
	form = Schools()
	if(request.method == 'POST'):
		choice = getschoolchoice(request) #Converted the school object to string for url formatting
		return redirect('school', school = choice)
	
	return render(request, 'temperatures/welcome.html', {'form':form})

#This view displays all the temperature readings of a particular school and 
def detail(request, school):
	url = 'schools/' + school + '/index.html'
	readings = TempReading.objects.filter(school=school)
	context = {'context': readings}
	return render(request, url, context)

#This view is used to filter queries on a schools detail page. AKA lets the user sort between readings from the past 30 days to the past 7 days etc.
def refreshdetail(request):
	filter = request.POST.get('filteroptions')
	filter = int(filter)
	start_date = datetime.datetime.now()
	end_date = datetime.datetime.today() - datetime.timedelta(days=filter)
	data = TempReading.objects.filter(date__lte=start_date, date__gte=end_date)
	context = {'context': data}
	return render(request, 'refreshdetail.html', context) 
	
def getschoolchoice(request):
	if(request.method == 'POST'):
		choice = request.POST.get('schoolchoice')
		return choice