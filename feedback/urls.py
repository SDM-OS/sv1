from django.conf.urls import patterns,url
from feedback import views

urlpatterns = patterns('',
	url(r'^$', views.form, name="form"),
	url(r'^register/', views.register, name="register"),
)