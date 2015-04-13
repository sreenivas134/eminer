from django.conf.urls import patterns, include, url
from django.contrib import admin
from eminer import views
urlpatterns = patterns('',
    url(r'^$', views.BlogView, name = 'home'),
    url(r'^about/$', views.About, name = 'about'),
    url(r'^(?P<post_name>[\w\-]+)/$', views.BlogView, name = 'entry-detail'),
    url(r'^pages/(?P<count>[0-9])/$', views.BlogView, name = 'entry-detail'),
)
