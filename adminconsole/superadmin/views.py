from django.shortcuts import render

# Create your views here.
def superadmin(request):
    return render(request,'superadmin.html')
def createstaff(request):
    return render(request,'createstaff.html')
def staffaccess(request):
    return render(request,'staff-access.html')