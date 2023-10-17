from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')
def checkin(request):
    return render(request,'checkin.html')
def attendanced(request):
    return render(request,'attendanced.html')