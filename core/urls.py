from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
     url(r'^$', views.index),
     url(r'^submit/', views.index),
)
