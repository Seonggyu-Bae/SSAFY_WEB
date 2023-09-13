from django.shortcuts import render

# Create your views here.

def price(request,thing,cnt):
    product_price = {"라면":980,"홈런볼":1500,'칙촉':2300, "식빵":1800}
    
    if thing in product_price:
        context = {
            'ispossible' : True,
            'thing' : thing,
            'cnt' : cnt,
            'totalprice' : product_price[thing] * cnt
            
        }
    else:
        context = {
        'ispossible' : False,
        'thing' : thing,
        'cnt' : cnt,
        'totalprice' : '없어용'
        
        }

    

    return render(request,'prices/price.html',context)