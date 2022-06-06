from django.urls import path
from myapp.views import *
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', index, name='index'),
    url(r'^User/$',list_user,name='list_user'),
    url(r'^User/create/$', user_create, name='user_create'),
]