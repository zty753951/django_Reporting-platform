from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles


urlpatterns=[
    url(r'^$',views.index),
]

