from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'opening_time', 'closing_time', 'logo']

		widgets = {
			'opening_time' : forms.TimeInput(attrs={'type':'time'}),
			'closing_time' : forms.TimeInput(attrs={'type':'time'}),
		}

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['restaurant','name','description','price','active']

class UserSignup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

		widgets = {
		'password': forms.PasswordInput() 
		}

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())