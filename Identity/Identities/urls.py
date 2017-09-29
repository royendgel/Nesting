from django.conf.urls import url 
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
	
	url(r'^$', views.nest, name = 'nest'),
	
	url(r'^login/$', login, {'template_name' : 'Identities/login.html'}, name = 'login'),
	
	url(r'^logout/$', login, {'template_name' : 'Identities/logout.html'}, name = 'logout'),
	
	url(r'^register/$', views.register, name = 'register'),
	
	
]