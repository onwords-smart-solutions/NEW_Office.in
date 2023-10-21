from django.shortcuts import render
from adminconsole.views import db, checkUserName

# Create your views here.
def superadmin(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    context = {
        "name":name,
        "dep":dep,
    }
    return render(request,'superadmin.html',context)
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