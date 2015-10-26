from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^order/(?P<id>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^add/$', views.order_add, name='order_add'),
]

