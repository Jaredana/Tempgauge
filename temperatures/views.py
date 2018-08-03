# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TempReading, School
from django.utils import timezone

# Create your views here.
def index(request):
	alltemps = TempReading.objects.all()
	context = {'foobar': alltemps}
	return render(request, 'temperatures/index.html', context)
