from django.shortcuts import render
from authapp.forms import UserForm, PizzaShopForm
# Create your views here.

def home(request):
    return render(request, 'authapp/home.html')

def authapp_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()
    return render(request, 'authapp/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })