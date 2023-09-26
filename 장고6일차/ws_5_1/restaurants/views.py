from django.shortcuts import render,redirect
from .models import Restaurant
# Create your views here.

def index(request):
    info = Restaurant.objects.all()
    context = {
        'info' : info,
    }
    return render(request,'restaurants/index.html',context)

def new(request):

    return render(request, 'restaurants/new.html')


def create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')

    info = Restaurant()
    info.name = name
    info.description = description
    info.address = address
    info.phone_number = phone_number
    info.save()
    return redirect('restaurants:index')