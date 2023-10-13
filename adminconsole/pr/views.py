from django.shortcuts import render

# Create your views here.

def prhome(request):
    return render(request,'prhome.html')
def create_lead(request):
    return render(request,'createLead.html')
def customer_details(request):
    return render(request,'customer_details.html')
def points_workdone(request):
    return render(request,'points_workdone.html')