from django.conf.urls import patterns, include, url
from django.contrib import admin
from eminer import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^blog/', include('eminer.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('eminer.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
