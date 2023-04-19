from django.forms.models import inlineformset_factory
from django import forms
from account import models
from account.models import Book_Demo,Book_Appointment,Super
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class demoFrom(forms.ModelForm):
	username = forms.CharField(max_length=20)
	mobile = forms.IntegerField()
	email = forms.EmailField(max_length=20)
	Company = forms.CharField(max_length=20)


	class Meta():
		"""docstring for Meta"""
		model = Book_Demo
		fields = ('username',
			      'mobile',
			      'email',
			      'Company',)


class appointmentFrom(forms.ModelForm):
	name=forms.CharField(max_length=100)
	email=forms.EmailField(max_length=100)
	phone=forms.IntegerField()
	date=forms.DateField()
	your_schedule=forms.CharField(max_length=100)
	your_time=forms.CharField(max_length=100)
	message=forms.CharField(max_length=100)


	class Meta():
		"""docstring for Meta"""
		model = Book_Appointment
		fields = ('name',
			      'email',
			      'phone',
			      'date',
			      'your_schedule',
			      'your_time',)




class appFrom(forms.ModelForm):

	
	slots=(('online','online'),('offline','offline'))
	Mode_type = forms.ChoiceField(choices=slots)
	no_demo = forms.IntegerField()
	classid = forms.IntegerField()
	date = forms.DateField()

		
		
	class Meta():
		"""docstring for Meta"""
		model = Super
		fields = ('Mode_type',
			      'no_demo',
			      'classid',
			      'date',)
