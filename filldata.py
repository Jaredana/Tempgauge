import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tempgauge.settings")
application = get_wsgi_application()
from django.apps import apps
from temperatures.models import TempReading
from django.utils import timezone


a = TempReading(temp = 53, date = timezone.now(), humidity = 21)
b = TempReading(temp = 57, date = timezone.now(), humidity = 24)
c = TempReading(temp = 55, date = timezone.now(), humidity = 23)
a.save()
b.save()
c.save()
all_entries = TempReading.objects.all()