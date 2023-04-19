from django.urls import path
from django.conf.urls import url
from account import views 

urlpatterns =[ 
path('registration',views.registration, name='registration'),
path('login',views.login, name='login'),
path('demo',views.demo, name='demo'),
path('logout',views.logout, name='logout'),
path('appointment',views.appointment, name='appointment'),
path('app',views.app, name='app'),
path('bookdemo',views.bookdemo, name='bookdemo'),
path('userbooking',views.userbooking, name='userbooking'),
path('',views.base,name='base'),
	
]