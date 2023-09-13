import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    empty_list = []
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }

    return render(request, 'articles/dinner.html', context)

def search(request):

    return render(request,'articles/search.html')


def throw(requset):

    return render(requset,'articles/throw.html')

def catch(requset):
    # 사용자로부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 , catch 템플릿에 출력
    
    message = requset.GET.get('message')
    context = {
        'message' :  message

    }
    return render(requset,'articles/catch.html',context)

def greeting(request, name):
    context = {
        'name' : name,

    }
    return render(request,'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }

    return render(request,'articles/detail.html',context)


def caculation(request):
  

    return render(request,'articles/caculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    if num2 != 0:
        context = {
            'num1' : num1,
            'num2' : num2,
            'sub' : num1 - num2,
            'mul' : num1 * num2,
            'div' : num1 / num2
        }
    else:
        context = {
            'num1' : num1,
            'num2' : num2,
            'sub' : num1 - num2,
            'mul' : num1 * num2,
        }

    return render(request,'articles/result.html',context)