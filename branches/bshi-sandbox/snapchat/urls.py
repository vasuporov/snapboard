# vim: ai ts=4 sts=4 et sw=4
from django.conf.urls.defaults import *

from views import rpc, index

urlpatterns = patterns('',
    (r'^rpc/$', rpc),
    (r'^', index),
)
