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
    sabin = 'SAB'
    schoolnames = (
            (sabin, 'Sabin'),
    )
    schoolchoice = models.CharField(
            max_length = 40,
            choices = schoolnames,
            default = sabin,
    )
    def __str__(self):
        return self.schoolchoice

