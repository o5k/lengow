from django.conf.urls import url, include
from rest_framework import routers
from . import views
from .viewsets import OrderViewSet


router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^order/(?P<id>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^add/$', views.order_add, name='order_add'),
    url(r'^update/(?P<id>[0-9]+)/$', views.order_update, name='order_update'),
    url(r'^api/', include(router.urls)),
]

