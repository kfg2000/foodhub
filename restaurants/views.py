from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Item 
from .forms import RestaurantForm, ItemForm, UserSignup, UserLogin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.utils import timezone 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def usersignup(request):
    context = {}
    form = UserSignup()
    context["form"] = form 
    if request.method == "POST":
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password

            user.set_password(password)
            user.save()

            auth = authenticate(username=username, password=password)
            login(request, auth)

            return redirect('list')
        messages.error(request, form.errors)
        return redirect("signup")
    return render(request,"signup.html",context)

def userlogin(request):
    context = {}
    form = UserLogin()
    context["form"] = form 
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth = authenticate(username=username, password=password)
            if auth is not None:
                login(request,auth)
                return redirect('list')
            
            messages.error(request, "Wrong username/password combination. Please try again.")
            return redirect("login")

        messages.error(request, form.errors)
        return redirect("login")
    return render(request,"login.html",context)


def userlogout(request):
    logout(request)
    return redirect("list")



def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    query = request.GET.get("q")
    if query:
        restaurants = restaurants.filter(name__icontains=query)

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

def restaurant_detail(request,restaurant_slug):
    time = timezone.now().time()
    restaurant = get_object_or_404(Restaurant, slug = restaurant_slug)
    items = restaurant.item_set.all()
    if not request.user.is_staff:
        items = restaurant.item_set.filter(active=True)
    context = {
    'item': restaurant,
    'items': items,
    'hour':time,
    }
    return render(request, 'restaurant_detail.html',context)


def restaurant_create(request):
    if not request.user.is_staff:
        raise Http404
    form = RestaurantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {
    'new': form,
    }
    return render(request,"restaurant_create.html",context)

def restaurant_update(request,restaurant_slug):
    if not request.user.is_staff:
        raise Http404
    restaurant = Restaurant.objects.get(slug=restaurant_slug)
    form = RestaurantForm(request.POST or None, request.FILES or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_slug=restaurant.slug)
    context = {
    'update': form,
    'item': restaurant,
    } 
    return render(request,"restaurant_update.html",context)

def restaurant_delete(request,restaurant_slug):
    if not request.user.is_staff:
        raise Http404
    item = Restaurant.objects.get(slug=restaurant_slug).delete()
    return redirect("list")

def item_create(request):
    if not request.user.is_staff:
        raise Http404
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {
    'new': form,
    }
    return render(request,"item_create.html",context)

def item_update(request,item_slug):
    if not request.user.is_staff:
        raise Http404
    item = Item.objects.get(slug=item_slug)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {
    'update': form,
    'item': item,
    }
    return render(request,"item_update.html",context)

def item_delete(request,item_slug):
    if not request.user.is_staff:
        raise Http404
    item = Item.objects.get(slug=item_slug).delete()
    return redirect("list")
    