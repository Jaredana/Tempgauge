# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TempReading, School
# Register your models here.
admin.site.register(TempReading)
admin.site.register(School)