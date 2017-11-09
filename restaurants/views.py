from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant 
from .forms import RestaurantForm
# Create your views here.
def restaurant_list(request):
	item = Restaurant.objects.all()
	context = {
	'items': item
	}
	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request,restaurant_id):
	item = get_object_or_404(Restaurant, id = restaurant_id)
	context = {
	'item': item,
	}
	return render(request, 'restaurant_detail.html',context)


def restaurant_create(request):
	form = RestaurantForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("list")
	context = {
	'form': form,
	}
	return render(request,"restaurant_create.html",context)

def restaurant_update(request,restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_id=item.id)
	context = {
	'form': form,
	'item': item,
	}
	return render(request,"restaurant_update.html",context)

def restaurant_delete(request,restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id).delete()
	return redirect("list")
	