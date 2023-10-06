from django.shortcuts import render

# Create your views here.

def ithome(request):
    return render(request,'ithome.html')