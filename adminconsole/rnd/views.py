from django.shortcuts import render
from adminconsole.views import db, checkUserName

# Create your views here.

def rndhome(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    context = {
        "name":name,
        "dep":dep,
    }
    return render(request,'rndhome.html',context)
def inprocess(request):
    return render(request,'inprocess.html')
def create(request):
    return render(request,'create.html')