from django.db import models
from django.contrib.auth.models import User,auth
from django import forms
# Create your models here.


class Book_Demo(models.Model):
	username=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	mobile=models.IntegerField()
	Company=models.CharField(max_length=100)

	def __str__(self):
		return self.username

class Book_Appointment(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	phone=models.IntegerField()
	date=models.DateField()
	your_schedule=models.CharField(max_length=100)
	your_time=models.CharField(max_length=100)
	message=models.CharField(max_length=100)

	def __str__(self):
		return self.name




class Super(models.Model):
	
	Mode_type = models.CharField(max_length=20,default=None)
	no_demo = models.IntegerField()
	classid = models.IntegerField()
	date = models.DateField()

	
	
	def __str__(self):
		return str(self.date)
				
class Reservation(models.Model):
	
	user_details = models.ForeignKey( User,on_delete=models.DO_NOTHING, null=False, blank=False)
	Mode_type = models.CharField(max_length=20, default=None)
	superData =  models.ForeignKey(Super, on_delete=models.CASCADE, null=False, blank=False)
	class Meta:
		verbose_name_plural ='Reservation'
		db_table = 'OGHBS_Reservation'
		ordering = ['user_details']

	def __str__(self):
		return str(self.user_details)
	
