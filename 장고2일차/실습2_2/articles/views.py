from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    #  사용자가 던진 데이터 받아오기
    # 요청 객체에서 꺼내오기
    name = request.GET.get('name')
    context = {
        'name' : name
    }

    return render(request, 'articles/catch.html',context)