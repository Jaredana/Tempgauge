import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tempgauge.settings")
application = get_wsgi_application()
from django.apps import apps
from temperatures.models import TempReading, School
from django.utils import timezone

choice = 0

def choose_school():
	schools = ['Sabin', 'Schellenberg', 'Milwaukie', 'Putnam']
	print('Choose a school: ')
	print('1.Sabin')
	print('2.Schellenberg')
	print('3.Milwaukie')
	print('4.Putnam')
	choice = schools[(int(input())) - 1]
	return choice

def create_tempreading():
	date = timezone.now()
	print('Enter the temperature: ')
	temp = int(input())
	print('Enter the Humidity: ')
	humidity = int(input())
	school = choose_school()
	a = TempReading(temp=temp, date=date, school=school, humidity=humidity)
	a.save()

def create_school():
	print('Enter a school name: ')
	choice = str(input())
	a = School(schoolname=choice)
	a.save()
	
while(choice != 6):
	print('Enter your choice')
	print('1.Add reading')
	print('2.Add School')
	print('3.Clear Readings')
	print('4.Clear Schools')
	print('6.Quit')
	choice = int(input())
	if(choice == 1):
		create_tempreading()
	elif(choice == 2):
		create_school()
	elif(choice == 6):
		print('Bye!')
	else:
		print('Invalid choice: try again!')
		choice = 0



	
# a = TempReading(temp = 53, date = timezone.now(), humidity = 21)
# b = TempReading(temp = 57, date = timezone.now(), humidity = 24)
# c = TempReading(temp = 55, date = timezone.now(), humidity = 23)
# a.save()
# b.save()
# c.save()
# all_entries = TempReading.objects.all()