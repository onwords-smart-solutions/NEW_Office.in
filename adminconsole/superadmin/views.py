from django.shortcuts import render
from django.shortcuts import redirect
from adminconsole.views import db, checkUserName
from django.http import HttpResponse, JsonResponse
from adminconsole.views import db, auth, checkUserName
from datetime import datetime,timedelta
# Create your views here.
def superadmin(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    name = checkUserName(uid)
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
    current_date1 = datetime.now().strftime("%d")
    current_date_today = datetime.now().strftime("%Y-%m-%d")
    current_date = datetime.now()

    staff=db.child("staff").get().val()
    attendance=db.child("attendance").child(current_year).child(current_month).get().val()
    stafftotalpresent=0
    stafftotalabsent=0
    for staffuid in staff:
        if staff[staffuid]["department"] != "ADMIN":
            try:
                attendance[current_date1][staffuid]
                stafftotalpresent=stafftotalpresent+1
            except:
                stafftotalabsent=stafftotalabsent+1
    inventory=db.child("inventory_management").get().val()
    inventoryall=[]
    for uid in inventory:
        inventoryall.append(inventory[uid])

    context={
        "name":name,
        "dep":dep,
        "profile":profile,
        "inventoryall":inventoryall,
        "stafftotalpresent":stafftotalpresent,
        "stafftotalabsent":stafftotalabsent
    }            
    return render(request,'superadmin.html',context)

def createstaff(request):
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1

    if request.method == "POST":
        try:
            _name = request.POST["name"]
            _email = request.POST["email"]
            _department = request.POST["department"]
            _password = request.POST["password"]
            try:
                _pt = request.POST["pt"]
                data = {
                    "name": _name,
                    "email": _email,
                    "department": _department,
                    "partTime": True,
                }
            except:
                data = {
                    "name": _name,
                    "email": _email,
                    "department": _department,
                }
            usr = auth.create_user_with_email_and_password(_email,_password)
            db.child("staff").child(usr["localId"]).set(data)
            auth.send_password_reset_email(_email)
            return render(
                request,
                "createstaff.html",
                {"message": "User Created Successfully"},
            )
        except:
            return HttpResponse("error creating user")
    else:
        return render(request, "createstaff.html",{"suggestionNotification":suggestionNotification})

def staffaccess(request):
    return render(request,'staff-access.html')
def userdata(request):
    return render(request,'userdata.html')
def viewsuggestion(request):
    # suggestionNotification = 0
    # suggestionData = db.child("suggestion").get().val()
    # for suggestion in suggestionData:
    #         if not suggestionData[suggestion]["isread"]:
    #             suggestionNotification += 1
    dList = []
    data = db.child('suggestion').get().val()
    try:
        for d in data:
            dList.append(data[d])
    except:
        pass
    context = {
        "sugg":dList,
        # "suggestionNotification": suggestionNotification
    }
    return render(request,'viewsuggestion.html',context)

def markasread(request):
    if request.method == "POST":
        message = request.POST["message"]
        date = request.POST["date"]
        time = request.POST["time"]
        suggestionData = db.child("suggestion").get().val()
        for d in suggestionData:
            if message == suggestionData[d]["message"]:
                db.child("suggestion").child(d).update({"isread":True})
            elif date == suggestionData[d]['date'] and time == suggestionData[d]['time']:
                db.child("suggestion").child(d).update({"isread":True})
        return redirect(viewsuggestion)
    return redirect("/")

def viewworkmanager(request):
    return render(request,'viewworkmanager.html')