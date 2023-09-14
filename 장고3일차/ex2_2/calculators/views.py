from django.shortcuts import render

# Create your views here.

def calculator(request,num1,num2):
    ispossible = True
    if num2 == 0:
        ispossible = False
    if ispossible:
        context = {
            'ispossible' : ispossible,
            'num1' : num1,
            'num2' : num2,
            'mul' : num1 * num2,
            'sub' : num1 - num2,
            'div' : num1 / num2,

        }
    else:
        context = {
            'ispossible' : ispossible,
            'num1' : num1,
            'num2' : num2,
            'mul' : num1 * num2,
            'sub' : num1 - num2,
        }
    return render(request,'calculators/calculator.html',context)