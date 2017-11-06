from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.restaurant_list, name = 'list'),
    url(r'^detail/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name = 'detail'),
]
