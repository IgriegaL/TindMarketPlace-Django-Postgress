from django import forms
from django.contrib.auth.models import User
from .models import Product, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name' , 'email', 'password')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'tema','price')

