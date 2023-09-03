from django.shortcuts import render

def boat1(request):
    return render(request,'boat1.html')

def home(request):
    return render(request,'home.html')