from django.shortcuts import render

def login(request):
    return render(request,'login.html')
def leave_form(request):
    return render(request,'leave-form.html')
def late_form(request):
    return render(request,'late_form.html')