from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^comm/', include('comm.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include(admin.site.urls)),
)
