from django.http import HttpResponse
from django.shortcuts import render
from .models import place, member


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = member.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     result1=x+y
#     result2=x-y
#     result3=x*y
#     result4=x/y
#     return render(request,"result.html",{'result11':result1,'result22':result2,'result33':result3,'result44':result4})
