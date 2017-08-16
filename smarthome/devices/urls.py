from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$', Home, name='home'),
	url(r'^actiondevice/$',ActionDevice,name='actiondevice'),
        url(r'^coontroltotal/$',ControlTotal,name='controltotal'),

]
