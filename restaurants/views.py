from django.shortcuts import render, get_object_or_404
from .models import Restaurant 
# Create your views here.
def restaurant_list(request):
	kao = Restaurant.objects.all()
	context = {
	'stuff': kao
	}
	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request,restaurant_id):
	detail = get_object_or_404(Restaurant, id = restaurant_id)
	context = {
	'kao': detail
	}
	return render(request, 'restaurant_detail.html',context)