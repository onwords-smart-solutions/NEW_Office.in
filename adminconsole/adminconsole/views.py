from django.shortcuts import render

def login(request):
    
    return render(request,'signin.html')
def leave_form(request):
    return render(request,'leave-form.html')