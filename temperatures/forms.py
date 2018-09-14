from django import forms
from temperatures.models import School

class Schools(forms.Form):
	schoolnames = School.objects.all()
	schoolchoice = forms.ModelChoiceField(queryset=schoolnames,empty_label='(nothing)', label = 'School', to_field_name='schoolname')
	def __iter__(self):
		return self.my_list
	