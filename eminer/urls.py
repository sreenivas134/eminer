from django.conf.urls import url, patterns
from eminer import views
urlpatterns=('',
             url(r'^$', views.BlogView, name='home'),
             
            )