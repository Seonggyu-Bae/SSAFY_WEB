from django.shortcuts import render
# Create your views here.

def food(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    context = {
        'foods' : food,
    }
    return render(request,'menus/food.html/',context)


def drink(request):
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    context = {
        'drinks' : drink,
    }
    return render(request,'menus/drink.html/',context)


def receipt(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    ordered_food = request.GET.get('message')
    ordered_drink = request.GET.get('message').lower()
    is_possible = False
    
    if ordered_food in food:
        is_possible = True
    if ordered_drink in drink:
         is_possible = True
    context = {
        'ordered_food' : ordered_food,
        'ordered_drink' : ordered_drink,
        'ispossible' : is_possible

    }
    return render(request,'menus/receipt.html/', context)