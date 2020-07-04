from django.conf.urls import url

from .views import (
        ProductListView,
        
        # ProductDetailView,
        SingleView
        # ProductSlideView
        )

urlpatterns = [
    url(r'^products/$', ProductListView, name='products'),
    # url(r'^products/$', ProductListView1.as_view(), name='prod'),
    # url(r'^slider/$', ProductSlideView),

    url(r'^view/(?P<slug>[\w-]+)/$', SingleView, name='view')
]