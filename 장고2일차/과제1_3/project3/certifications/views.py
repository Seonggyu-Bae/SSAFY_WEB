from django.shortcuts import render
from . import data
import random
# Create your views here.

def certification1(request):
    context = {
        'name' : 'kim happy',
        'age' : data.age,
        'grade' : data.grade
    }
    return render(request,'certifications/certification1.html',context)

def certification2(request):
    context = {
        'name' : 'park happy',
        'age' : data.age,
        'grade' :  data.grade
    }
    return render(request,'certifications/certification2.html',context)

def certification3(request):
    context = {
        'name' : 'lee happy',
        'age' : data.age,
        'grade' :  data.grade
    }
    return render(request,'certifications/certification3.html',context)