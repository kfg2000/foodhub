from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.restaurant_list, name = 'list'),
    url(r'^detail/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_detail, name = 'restaurant_detail'),
    url(r'^create/$', views.restaurant_create, name = 'restaurant_create'),
    url(r'^update/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_update, name = 'restaurant_update'),
    url(r'^delete/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_delete, name = 'restaurant_delete'),
    url(r'^itemCreate/$', views.item_create, name = 'item_create'),
    url(r'^itemUpdate/(?P<item_slug>[-\w]+)/$', views.item_update, name = 'item_update'),
    url(r'^itemDelete/(?P<item_slug>[-\w]+)/$', views.item_delete, name = 'item_delete'),
    url(r'^signup/$', views.usersignup, name = 'signup'),
    url(r'^login/$', views.userlogin, name = 'login'),
    url(r'^logout/$', views.userlogout, name = 'logout'),
]
