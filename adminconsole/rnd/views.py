from django.shortcuts import render

# Create your views here.

def rndhome(request):
    return render(request,'rndhome.html')
def inprocess(request):
    return render(request,'inprocess.html')
def create(request):
    return render(request,'create.html')