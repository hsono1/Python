from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success, name = "success"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = "remove"),

]
