from django.conf.urls import url
from .views import (
    # initiate_payment,
    # callback,
    razor_pay,
    payment_status
    )

urlpatterns = [
    #    url(r'^pay/$', initiate_payment, name='payment'),
    #    url(r'^callback/$', callback, name='callback'),
       url(r'^razor/$', razor_pay, name='razor'),
       url(r'^payment_status/$', payment_status, name='payment_status')
]