from django.shortcuts import render

# Create your views here.

def first(request):
    throw = request.GET.get('throw')
    context = {
        'catch' : throw
    }
    return render(request, 'throw_catch/first.html/', context)


def second(request):
    throw = request.GET.get('throw')
    context = {
        'catch' : throw
    }
    return render(request, 'throw_catch/second.html/', context)
