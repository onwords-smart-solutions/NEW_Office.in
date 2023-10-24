from django.shortcuts import render
from django.shortcuts import redirect
from adminconsole.views import db, checkUserName
from django.http import HttpResponse, JsonResponse
from adminconsole.views import db, auth, checkUserName
from datetime import datetime,timedelta,date
import requests
# Create your views here.

def superadmin(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    name = request.COOKIES["name"]
    webaccess=db.child("webaccess").get().val()
    general,customeracccess,accountacccess,createleadacccess,createstaffacccess,inventoryacccess,prdashboardacccess,quotationacccess,userdataacccess,viewsuggestionacccess,viewmanageracccess,approvalacccess,inprogressacccess=False,False,False,False,False,False,False,False,False,False,False,False,False
    for accessuid in webaccess["customer details"]:
        if webaccess["customer details"][accessuid] == uid:
            customeracccess=True

    for accessuid in webaccess[ "Account"]:
        if webaccess[ "Account"][accessuid] == uid:    
            accountacccess=True

    for accessuid in webaccess["Create Lead"]:
        if webaccess["Create Lead"][accessuid] == uid:    
            createleadacccess=True

    for accessuid in webaccess["Create Staff"]:
        if webaccess["Create Staff"][accessuid] == uid:    
            createstaffacccess=True

    for accessuid in webaccess["Inventory Page"]:
        if webaccess["Inventory Page"][accessuid] == uid:    
            inventoryacccess=True

    for accessuid in webaccess["Prdashboard"]:
        if webaccess["Prdashboard"][accessuid] == uid:
            prdashboardacccess=True

    for accessuid in webaccess["Quotation Page"]:
        if webaccess["Quotation Page"][accessuid] == uid:
            quotationacccess=True

    for accessuid in webaccess["User Data"]:
        if webaccess["User Data"][accessuid] == uid:
            userdataacccess=True

    for accessuid in webaccess["View Suggestion"]:
        if webaccess["View Suggestion"][accessuid] == uid:
            viewsuggestionacccess=True

    for accessuid in webaccess[ "Viewwork Manager"]:
        if webaccess[ "Viewwork Manager"][accessuid] == uid:
            viewmanageracccess=True

    for accessuid in webaccess["approval"]:
        if webaccess["approval"][accessuid] == uid:
            approvalacccess=True

    for accessuid in webaccess["inprogress"]:
        if webaccess["inprogress"][accessuid] == uid:
            inprogressacccess=True            
    if uid is not None:
        general=True

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
        "stafftotalabsent":stafftotalabsent,
        "general":general,
        "approvalpage":approvalacccess,
        "rnd":inprogressacccess,
        "account":accountacccess,
        "createlead":createleadacccess,
        "customerdetails":customeracccess,
        "quotation":quotationacccess,
        "inventory":inventoryacccess,
        "createstaff":createstaffacccess,
        "viewworkmanager":viewmanageracccess,
        "viewsuggestion":viewsuggestionacccess,
        "userdata":userdataacccess,
        "prdashboard":prdashboardacccess,  
    }            
    return render(request,'superadmin.html',context)

def createstaff(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    name = request.COOKIES["name"]
    webaccess=db.child("webaccess").get().val()
    general,customeracccess,accountacccess,createleadacccess,createstaffacccess,inventoryacccess,prdashboardacccess,quotationacccess,userdataacccess,viewsuggestionacccess,viewmanageracccess,approvalacccess,inprogressacccess=False,False,False,False,False,False,False,False,False,False,False,False,False
    for accessuid in webaccess["customer details"]:
        if webaccess["customer details"][accessuid] == uid:
            customeracccess=True

    for accessuid in webaccess[ "Account"]:
        if webaccess[ "Account"][accessuid] == uid:    
            accountacccess=True

    for accessuid in webaccess["Create Lead"]:
        if webaccess["Create Lead"][accessuid] == uid:    
            createleadacccess=True

    for accessuid in webaccess["Create Staff"]:
        if webaccess["Create Staff"][accessuid] == uid:    
            createstaffacccess=True

    for accessuid in webaccess["Inventory Page"]:
        if webaccess["Inventory Page"][accessuid] == uid:    
            inventoryacccess=True

    for accessuid in webaccess["Prdashboard"]:
        if webaccess["Prdashboard"][accessuid] == uid:
            prdashboardacccess=True

    for accessuid in webaccess["Quotation Page"]:
        if webaccess["Quotation Page"][accessuid] == uid:
            quotationacccess=True

    for accessuid in webaccess["User Data"]:
        if webaccess["User Data"][accessuid] == uid:
            userdataacccess=True

    for accessuid in webaccess["View Suggestion"]:
        if webaccess["View Suggestion"][accessuid] == uid:
            viewsuggestionacccess=True

    for accessuid in webaccess[ "Viewwork Manager"]:
        if webaccess[ "Viewwork Manager"][accessuid] == uid:
            viewmanageracccess=True

    for accessuid in webaccess["approval"]:
        if webaccess["approval"][accessuid] == uid:
            approvalacccess=True

    for accessuid in webaccess["inprogress"]:
        if webaccess["inprogress"][accessuid] == uid:
            inprogressacccess=True            
    if uid is not None:
        general=True

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
            context={
                    "message": "User Created Successfully",
                    "name":name,
                    "dep":dep,
                    "profile":profile,
                    "general":general,
                    "approvalpage":approvalacccess,
                    "rnd":inprogressacccess,
                    "account":accountacccess,
                    "createlead":createleadacccess,
                    "customerdetails":customeracccess,
                    "quotation":quotationacccess,
                    "inventory":inventoryacccess,
                    "createstaff":createstaffacccess,
                    "viewworkmanager":viewmanageracccess,
                    "viewsuggestion":viewsuggestionacccess,
                    "userdata":userdataacccess,
                    "prdashboard":prdashboardacccess,
            }
            return render(request,"createstaff.html",context)
        except:
            return HttpResponse("error creating user")
    else:
        context={
            "suggestionNotification":suggestionNotification,
            "name":name,
            "dep":dep,
            "profile":profile,
            "general":general,
            "approvalpage":approvalacccess,
            "rnd":inprogressacccess,
            "account":accountacccess,
            "createlead":createleadacccess,
            "customerdetails":customeracccess,
            "quotation":quotationacccess,
            "inventory":inventoryacccess,
            "createstaff":createstaffacccess,
            "viewworkmanager":viewmanageracccess,
            "viewsuggestion":viewsuggestionacccess,
            "userdata":userdataacccess,
            "prdashboard":prdashboardacccess,
            }
        return render(request, "createstaff.html",context)

def staffaccess(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile = request.COOKIES["profile"]
    webaccess=db.child("webaccess").get().val()
    general,customeracccess,accountacccess,createleadacccess,createstaffacccess,inventoryacccess,prdashboardacccess,quotationacccess,userdataacccess,viewsuggestionacccess,viewmanageracccess,approvalacccess,inprogressacccess=False,False,False,False,False,False,False,False,False,False,False,False,False
    for accessuid in webaccess["customer details"]:
        if webaccess["customer details"][accessuid] == uid:
            customeracccess=True

    for accessuid in webaccess[ "Account"]:
        if webaccess[ "Account"][accessuid] == uid:    
            accountacccess=True

    for accessuid in webaccess["Create Lead"]:
        if webaccess["Create Lead"][accessuid] == uid:    
            createleadacccess=True

    for accessuid in webaccess["Create Staff"]:
        if webaccess["Create Staff"][accessuid] == uid:    
            createstaffacccess=True

    for accessuid in webaccess["Inventory Page"]:
        if webaccess["Inventory Page"][accessuid] == uid:    
            inventoryacccess=True

    for accessuid in webaccess["Prdashboard"]:
        if webaccess["Prdashboard"][accessuid] == uid:
            prdashboardacccess=True

    for accessuid in webaccess["Quotation Page"]:
        if webaccess["Quotation Page"][accessuid] == uid:
            quotationacccess=True

    for accessuid in webaccess["User Data"]:
        if webaccess["User Data"][accessuid] == uid:
            userdataacccess=True

    for accessuid in webaccess["View Suggestion"]:
        if webaccess["View Suggestion"][accessuid] == uid:
            viewsuggestionacccess=True

    for accessuid in webaccess[ "Viewwork Manager"]:
        if webaccess[ "Viewwork Manager"][accessuid] == uid:
            viewmanageracccess=True

    for accessuid in webaccess["approval"]:
        if webaccess["approval"][accessuid] == uid:
            approvalacccess=True

    for accessuid in webaccess["inprogress"]:
        if webaccess["inprogress"][accessuid] == uid:
            inprogressacccess=True            
    if uid is not None:
        general=True

    if request.method == "POST":
        uid = request.POST["uid"]
        access = request.POST["access"]
        web=db.child("webaccess").get().val()
        try:
            count=len(web[access])
            print(count)
        except:
            print('ll')
            count=0
        data={
            "uid"+str(count+1):uid
        }
        print(data)
        db.child("webaccess").child(access).update(data)
    staff=db.child("staff").get().val()
    namelist=[]
    uidlist=[]
    for uid in staff:
        namelist.append(staff[uid]["name"])
        uidlist.append(uid)
    allstaff=zip(uidlist,namelist) 
    context={
        "allstaff":allstaff,
        "name":name,
        "dep":dep,
        "profile":profile,
        "general":general,
        "approvalpage":approvalacccess,
        "rnd":inprogressacccess,
        "account":accountacccess,
        "createlead":createleadacccess,
        "customerdetails":customeracccess,
        "quotation":quotationacccess,
        "inventory":inventoryacccess,
        "createstaff":createstaffacccess,
        "viewworkmanager":viewmanageracccess,
        "viewsuggestion":viewsuggestionacccess,
        "userdata":userdataacccess,
        "prdashboard":prdashboardacccess,
    }   
    return render(request,'staff-access.html',context)

def viewsuggestion(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile = request.COOKIES["profile"]
    webaccess=db.child("webaccess").get().val()
    general,customeracccess,accountacccess,createleadacccess,createstaffacccess,inventoryacccess,prdashboardacccess,quotationacccess,userdataacccess,viewsuggestionacccess,viewmanageracccess,approvalacccess,inprogressacccess=False,False,False,False,False,False,False,False,False,False,False,False,False
    for accessuid in webaccess["customer details"]:
        if webaccess["customer details"][accessuid] == uid:
            customeracccess=True

    for accessuid in webaccess[ "Account"]:
        if webaccess[ "Account"][accessuid] == uid:    
            accountacccess=True

    for accessuid in webaccess["Create Lead"]:
        if webaccess["Create Lead"][accessuid] == uid:    
            createleadacccess=True

    for accessuid in webaccess["Create Staff"]:
        if webaccess["Create Staff"][accessuid] == uid:    
            createstaffacccess=True

    for accessuid in webaccess["Inventory Page"]:
        if webaccess["Inventory Page"][accessuid] == uid:    
            inventoryacccess=True

    for accessuid in webaccess["Prdashboard"]:
        if webaccess["Prdashboard"][accessuid] == uid:
            prdashboardacccess=True

    for accessuid in webaccess["Quotation Page"]:
        if webaccess["Quotation Page"][accessuid] == uid:
            quotationacccess=True

    for accessuid in webaccess["User Data"]:
        if webaccess["User Data"][accessuid] == uid:
            userdataacccess=True

    for accessuid in webaccess["View Suggestion"]:
        if webaccess["View Suggestion"][accessuid] == uid:
            viewsuggestionacccess=True

    for accessuid in webaccess[ "Viewwork Manager"]:
        if webaccess[ "Viewwork Manager"][accessuid] == uid:
            viewmanageracccess=True

    for accessuid in webaccess["approval"]:
        if webaccess["approval"][accessuid] == uid:
            approvalacccess=True

    for accessuid in webaccess["inprogress"]:
        if webaccess["inprogress"][accessuid] == uid:
            inprogressacccess=True            
    if uid is not None:
        general=True

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
        "name":name,
        "dep":dep,
        "profile":profile,
        "general":general,
        "approvalpage":approvalacccess,
        "rnd":inprogressacccess,
        "account":accountacccess,
        "createlead":createleadacccess,
        "customerdetails":customeracccess,
        "quotation":quotationacccess,
        "inventory":inventoryacccess,
        "createstaff":createstaffacccess,
        "viewworkmanager":viewmanageracccess,
        "viewsuggestion":viewsuggestionacccess,
        "userdata":userdataacccess,
        "prdashboard":prdashboardacccess,
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
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1
    # try:
    #     sensor = requests.get("http://117.247.181.113:8000/sensor/1/").json()
    #     eb_status = sensor["EB_Status"]
    # except:
    #     eb_status = "-"
    pendingWorkList, nameList, notWorkingList, absentList, presentList, presentTimeList = [], [], [], [], [], []
    pendingWorkList.clear()
    nameList.clear()
    notWorkingList.clear()
    absentList.clear()

    data = db.child("staff").get().val()
    todayDate = str(date.today())
    thisYear = datetime.now().strftime("%Y")
    thisMonth = datetime.now().strftime("%m")
    for staff in data:
        if not data[staff]["department"] == "ADMIN":
            fp = db.child("fingerPrint").get().val()
            try:
                fp[staff][todayDate]
                presentList.append(data[staff]["name"])
                for time in fp[staff][todayDate]:
                    presentTimeList.append(time)
                    break
            except:
                absentList.append(data[staff]["name"])
    nameWorkList = zip(nameList, pendingWorkList)
    lenWorking = len(nameList)
    lenNotWorking = len(notWorkingList)
    lenAbsent = len(absentList)
    present = zip(presentList, presentTimeList)
    presentMobile = zip(presentList, presentTimeList)
    context = {
        "lenWorking": lenWorking,
        "lenNotWorking": lenNotWorking,
        "lenAbsent": lenAbsent,
        "nameWorkList": nameWorkList,
        "notWorkingList": notWorkingList,
        "absentList": absentList,
        # "eb_status": eb_status,
        "todayDate": todayDate,
        "present": present,
        "presentMobile": presentMobile,
        "staffsPresent": len(presentList),
        "suggestionNotification":suggestionNotification
    }
    return render(request,'viewworkmanager.html',context)