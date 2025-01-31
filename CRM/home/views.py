from django.shortcuts import render,redirect
from django.urls import reverse
from items.models import Category,Item
from django.contrib.auth import logout

from .form import SignupForm
# Create your views here.
def index(request):
    item = Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    return render(request,"home/index.html",{
        'categories':category,
        'items':item,
    })

def contact(request):
    return render(request,"home/contact.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save() 
            print('form successful')        

            return redirect(reverse('home:login'))
    else:
        form = SignupForm()

    return render(request,'home/signup.html',{
        'form':form
    })

def user_logout(request):
    logout(request)
    return redirect('home:index')  # Redirect to the login page after logout
