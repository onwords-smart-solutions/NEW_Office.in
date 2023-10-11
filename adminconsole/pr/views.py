from django.shortcuts import render

# Create your views here.

def prhome(request):
    return render(request,'prhome.html')
def create_lead(request):
    return render(request,'createLead.html')