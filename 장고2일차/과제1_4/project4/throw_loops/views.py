from django.shortcuts import render

# Create your views here.

def first(request):
    message = request.GET.get('message')
    context = {
        'catch' : message

    }
    return render(request,'throw_loops/first.html',context)

def second(request):
    message = request.GET.get('message')
    context = {
        'catch' : message

    }
    return render(request,'throw_loops/second.html',context)

def third(request):
    message = request.GET.get('message')
    message1 = request.GET.get('message1')
    context = {
        'catch' : [message, message1]

    }
    return render(request,'throw_loops/third.html',context)

