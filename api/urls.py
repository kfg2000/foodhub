from django.conf.urls import url
from api.views import *

urlpatterns = [
	url(r'^list/$', RestaurantListAPIView.as_view(), name="list"),
	url(r'^detail/(?P<slug>[-\w]+)/$', RestaurantDetailAPIView.as_view(), name="detail"),
	url(r'^delete/(?P<slug>[-\w]+)/$', RestaurantDeleteAPIView.as_view(), name="delete"),
	url(r'^update/(?P<slug>[-\w]+)/$', RestaurantUpdateAPIView.as_view(), name="update"),
	url(r'^create/$', RestaurantCreateAPIView.as_view(), name="create"),
]