from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from account import models
from account.models import Book_Demo, Book_Appointment,Super, Reservation
import datetime
from account.forms import appFrom

# Create your views here.
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)
		if user is not None:
		  		auth.login(request,user)
		  		return redirect("base")
		else:
			messages.info(request,'invalid candentials')
			return redirect(login)	



	else:
		return render(request,'login.html')


def registration(request):
	if request.method =='POST':
	  	first_name=request.POST['first_name']
	  	last_name=request.POST['last_name']
	  	username=request.POST['username']
	  	password1=request.POST['password1']
	  	password2=request.POST['password2']
	  	email=request.POST['email']

	  	if password1==password2:
	  		if User.objects.filter(username=username).exists():
	  			print('username taken')
	  			messages.info(request,'username taken')
	  			return redirect('registration')


	  		elif User.objects.filter(email=email).exists():
	  			messages.info(request,'email taken')
	  			return redirect('registration')
	  		else:
		  		user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
			  	user.save();
			  	messages.info(request,'user created')
			  	return redirect('login')
	else:
	      print('password not matching..')
	     
	      return render(request,'registration.html')

def logout(request):
	auth.logout(request)
	return redirect('base')


def demo(request):
	if request.method =='POST':
	  	username=request.POST['username']
	  	mobile=request.POST['mobile']
	  	email=request.POST['email']
	  	Company=request.POST['Company']
	  

	  	uuser=Book_Demo.objects.create(Company=Company,email=email,username=username,mobile=mobile)
	  	uuser.save();
	  	messages.info(request,'request for demo is accepted')
	
	  	return redirect('base')
	else:		
		return render(request,'demo.html')


def appointment(request):
	if request.method =="POST":
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		date = request.POST['date']
		your_schedule = request.POST['your_schedule']
		your_time = request.POST['your_time']
		message = request.POST['message']

		vuser=Book_Appointment.objects.create(name=name,email=email,phone=phone,date=date,your_schedule=your_schedule,your_time=your_time,message=message)
		vuser.save();
		messages.info(request,'Your appointment is Succesfully booked')
		return redirect('base')

	else:
		return render(request,'appointment.html')

def app(request):
	if request.method =="POST":
		Mode_type = request.POST['Mode_type']
		date = request .POST['date']
		classid = request.POST['classid']
		no_demo = request.POST['no_demo']
		wuser=Super.objects.create(Mode_type=Mode_type,date=date,no_demo=no_demo,classid=classid)
		wuser.save();
		messages.info(request,' Demo Shedule is Created ')
		return redirect('app')


	else:
		supers = Super.objects.all()
		context = {'x': supers}


	return render(request,'app.html', context)

def bookdemo(request):
	supers = Super.objects.all()
	return render(request,'bookdemo.html',{'supers':supers})	

def userbooking(request):
	reservations =  Reservation.objects.all()
	form = appFrom()
	return render(request,'userbooking.html',{'reservations':reservations, 'form':form})

def base(request):
	return render(request,'base.html')