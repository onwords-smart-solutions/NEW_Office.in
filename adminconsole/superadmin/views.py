from django.shortcuts import render

# Create your views here.
def superadmin(request):
    return render(request,'superadmin.html')
def createstaff(request):
    return render(request,'createstaff.html')
def staffaccess(request):
    return render(request,'staff-access.html')
def userdata(request):
    return render(request,'userdata.html')
def viewsuggestion(request):
    return render(request,'viewsuggestion.html')
def viewworkmanager(request):
    return render(request,'viewworkmanager.html')