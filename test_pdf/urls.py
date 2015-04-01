from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^home$', 'monapp_pdf.views.home'),
)
