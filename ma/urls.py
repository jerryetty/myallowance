from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'myallowance'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^whyus/$', views.whyus, name='whyus'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^help/$', views.help, name='help'),
]