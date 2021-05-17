from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{'name':"Genesis"})

def display(request):
    name=request.GET["Name"]
    domain=request.GET["Domain"]
    result=name+" welcome to training on "+domain
    return render(request,"home.html",{"res":result})