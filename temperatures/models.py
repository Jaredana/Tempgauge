# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TempReading(models.Model):
    date = models.DateField('Date Recorded')
    temp = models.PositiveSmallIntegerField('Temperature')
    humidity = models.PositiveSmallIntegerField('Humidity')
    def __int__(self):
        return self.temp

class School(models.Model):
	schoolname = models.CharField(max_length=100, default='')
	def __str__(self):
		return self.schoolname