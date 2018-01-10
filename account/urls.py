from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#url(r'^login/$', views.user_login, name='login')
	url(r'^$', views.dashboard, name='dashboard'),
	#login / logout
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout-then-login'),
	#password urls
	url(r'^password-change/$', auth_views.password_change, name="password_change"),
	url(r'^password-change/done/$', auth_views.password_change_done, name="password_change_done"),
	# password reset urls
	url(r'^password-reset/$', auth_views.password_reset,
		{
			'template_name': 'registration/password_reset_form.html'
		}, 
		name="password-reset"),
	url(r'^password-reset/done/$', auth_views.password_reset_done, name="password_reset_done"),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^password-reset/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
	# user registration
	url(r'^register/$', views.register, name='register'),
	# edit urls
	url(r'^edit/$', views.edit, name="edit"),
]