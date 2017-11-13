from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant 
from .forms import RestaurantForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def restaurant_list(request):
	restaurants = Restaurant.objects.all()

	paginator = Paginator(restaurants,3)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	context = {
	'items': objects
	}
	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request,restaurant_id):
	restaurant = get_object_or_404(Restaurant, id = restaurant_id)
	context = {
	'item': restaurant,
	}
	return render(request, 'restaurant_detail.html',context)


def restaurant_create(request):
	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("list")
	context = {
	'new': form,
	}
	return render(request,"restaurant_create.html",context)

def restaurant_update(request,restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(request.POST or None, request.FILES or None, instance=restaurant)
	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_id=restaurant.id)
	context = {
	'update': form,
	'item': restaurant,
	}
	return render(request,"restaurant_update.html",context)

def restaurant_delete(request,restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id).delete()
	return redirect("list")
	