from django.conf.urls import url
from .views import (
    initiate_payment,
    callback
    )

urlpatterns = [
       url(r'^pay/$', initiate_payment, name='payment'),
       url(r'^callback/$', callback, name='callback')
]