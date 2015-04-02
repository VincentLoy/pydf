from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('monapp_pdf.views',
    url(r'^home$', 'home'),
    url(r'^reportlab$', 'py_df'),
)
