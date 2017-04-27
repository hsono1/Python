from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.welcome),
    url(r'^login$', views.login),
    url(r'^remove$', views.remove),
    url(r'^logout$', views.logout),
    
]
