from django.shortcuts import render

def homecopy(request):
    return render(request,'homecopy.html')

def home(request):
    return render(request,'home.html')