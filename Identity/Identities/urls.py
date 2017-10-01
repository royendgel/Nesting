from django.conf.urls import url 
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

from . import views

urlpatterns = [
	
	url(r'^$', views.nest, name = 'nest'),
	
	url(r'^login/$', login, {'template_name' : 'Identities/login.html'}, name = 'login'),
	
	url(r'^logout/$', login, {'template_name' : 'Identities/logout.html'}, name = 'logout'),
	
	url(r'^register/$', views.register, name = 'register'),
	
	url(r'^profile/$', views.view_profile, name = 'view_profile'),
	
	url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
	
	url(r'^change-password/$', views.change_password, name = 'change_password'),

	url(r'^reset-password/$', password_reset, name = 'reset_password'),
	
	url(r'^reset-password/done/$', password_reset_done, name = 'password_reset_done')
	
	
]