# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TempReading, School
from .forms import Schools
from django.utils import timezone

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
		#url = 'schools/' + choice + '/index.html'
		#return redirect(url)
		path = 'schools/' + choice
		print(choice)
		return redirect('school', school = choice)
	
	return render(request, 'temperatures/welcome.html', {'form':form})

def detail(request, school):
	url = 'schools/' + school + '/index.html'
	return render(request, url)
	
def getschoolchoice(request):
	choice = request.POST.get('schoolchoice')
	list = School.objects.all()
	choice = str(list[int(choice)- 1 ])
	return choice