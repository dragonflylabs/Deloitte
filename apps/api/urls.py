from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('apps.api.views',
    url(r'news/', 'news')
)
