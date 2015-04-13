from django.conf.urls import patterns, include, url
from django.contrib import admin
from eminer import views
urlpatterns = patterns('',
    url(r'^$', views.BlogView, name = 'home'),
    url(r'^about/$', views.About, name = 'about'),
)
