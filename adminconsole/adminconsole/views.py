from django.shortcuts import render, redirect
import pyrebase, requests
from datetime import date, datetime, timedelta, time
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pytz

config = {
    "apiKey": "AIzaSyCCTeiCYTB_npcWKKxl-Oj0StQLTmaFOaE",
    "authDomain": "marketing-data-d141d.firebaseapp.com",
    "databaseURL": "https://marketing-data-d141d-default-rtdb.firebaseio.com/",
    "storageBucket": "marketing-data-d141d.appspot.com",
}
firebaseConfig = {
  "apiKey": "AIzaSyBTcgfGrYDzHXN6aPyRP6LTIeRv-1w-Bio",
  "authDomain": "testadminconsole.firebaseapp.com",
  "projectId": "testadminconsole",
  "databaseURL":"https://testadminconsole-default-rtdb.firebaseio.com/",
  "storageBucket": "testadminconsole.appspot.com",
  "messagingSenderId": "982262166733",
  "appId": "1:982262166733:web:b14a765e30b114ba37a584",
  "measurementId": "G-PSYFW4L5W9"
}
aiconfig = {
    "apiKey": "AIzaSyAlNAm5qoM4SsK7Wrry5lbw7QndE_pBKa8",
    "authDomain": "onyx-9lbl.firebaseapp.com",
    "databaseURL": "https://onyx-9lbl-default-rtdb.firebaseio.com",
    "projectId": "onyx-9lbl",
    "storageBucket": "onyx-9lbl.appspot.com",
    "messagingSenderId": "365318702826",
    "appId": "1:365318702826:web:4a0b076ed7d7ee3b69b993",
    "measurementId": "G-J4YXBZGFJY",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
storage1 = firebase.storage()

firebase1 = pyrebase.initialize_app(firebaseConfig)
db1 = firebase1.database()
storage = firebase1.storage()

aifirebase = pyrebase.initialize_app(aiconfig)
aidb = aifirebase.database()
aiauth = aifirebase.auth()
aistorage = aifirebase.storage()

def login(request):
    try:
        uid = request.COOKIES["uid"]
        loginState = request.COOKIES["loginState"]
        if bool(loginState) == True:
            dep = checkUserDepartment(uid)
            if uid == "pztngdZPCPQrEvmI37b3gf3w33d2":
                print("inside redirect1")
                response = redirect("coohome") 
                return response 
            if uid == "A5kpLL2U0UaOkPrw2GeI8llH49s1" or uid == "yleZdWDZgFYTBxwzC5NtHVeb3733" or uid== "jDYzpwcpv3akKaoDL9N4mllsGCs2":
                response = redirect("adminhome") 
                return response
            if dep == "APP":
                response = redirect("ithome")
                return response
            if dep == "WEB":
                response = redirect("ithome")
                return response
            if dep == "MEDIA":
                response = redirect("ithome")
                return response
            if dep == "PR":
                print("pr dep")
                response = redirect("prhome")
                return response
            if dep == "RND":
                print("inside rnd")
                response = redirect("rndhome")
                return response
            if dep == "ADMIN":
                response = redirect("superadmin")
                return response
            if dep == "Installation":
                response = redirect("installationhome")
                return response
            if dep == "AIML":
                response = redirect("ithome")
                return response
            if dep == "HR":
                response = redirect("hrhome")
                return response
             
    except:
        pass

    if request.method == "POST":
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.sign_in_with_email_and_password(email, password)
            uid = user["localId"]  # to get the uid of the authentication
            dep = checkUserDepartment(uid)
            name = checkUserName(uid)
            profile=profileall(uid)
            exp = 100 * 365 * 24 * 60 * 60
            print("==log",uid)
            if uid == "pztngdZPCPQrEvmI37b3gf3w33d2":
                response = redirect("coohome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if uid == "A5kpLL2U0UaOkPrw2GeI8llH49s1" or uid == "yleZdWDZgFYTBxwzC5NtHVeb3733" or uid== "jDYzpwcpv3akKaoDL9N4mllsGCs2":
                response = redirect("adminhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "APP":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "WEB":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "MEDIA":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "PR":
                response = redirect("prhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "RND":
                print("inside rnd")
                response = redirect("rndhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "ADMIN":
                response = redirect("superadmin")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "Installation":
                response = redirect("installationhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "HR":
                response = redirect("hrhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("name", name, expires=exp)
                response.set_cookie("profile", profile, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            
            return redirect("login")
        except:
            context = {"error": "* The name or password you entered is incorrect."}
            return render(request, "login.html", context)
    else:
        return render(request, "login.html")
    

def leave_form(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    name = request.COOKIES["name"]
    leave_data = db.child("leave_details").get().val()
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
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
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        if leave_type == "general":
            try:
                try:
                    from_date = datetime.strptime(request.POST['fromdate'], '%Y-%m-%d')
                    to_date = datetime.strptime(request.POST['todate'], '%Y-%m-%d')
                   
                    reason = request.POST['reason']
                    c = {
                        "dep": dep,
                        "name": name,
                        "reason": reason,
                        "status": "Pending",
                        "node":"Full Day",
                    }
                    date_list = []

                    while from_date <= to_date:
                        date_list.append(from_date.strftime('%Y-%m-%d'))
                        from_date += timedelta(days=1)
                    for date in date_list:
                        year, month, day = map(int, date.split('-'))
                        c["date"] = date
                        if from_date == to_date:
                            db.child("leave_details").child(year).child(month).child(date).child(uid).child(leave_type).update(c)
                        else:
                            db.child("leave_details").child(year).child(month).child(date).child(uid).child(leave_type).update(c)
                except:
                    from_date = datetime.strptime(request.POST['fromdate'], '%Y-%m-%d') 
                    year, month, day = map(int, from_date.split('-'))
                    reason = request.POST['reason']
                    c = {
                        "dep": dep,
                        "name": name,
                        "reason": reason,
                        "status": "Pending",
                        "node":"Full Day",
                        "date":from_date,
                    }

                  
                    db.child("leave_details").child(year).child(month).child(from_date).child(uid).child(leave_type).update(c)    
            except:
                print("inside half")
                half_date = (request.POST.get('halfdate'))    
                reason = request.POST.get('reason')
                year, month, day = map(int, half_date.split('-'))

                c = {
                    "dep": dep,
                    "name": name,
                    "reason": reason,
                    "status": "Pending",
                    "node":"Half Day",
                    "date":half_date,
                }
                db.child("leave_details").child(year).child(month).child(half_date).child(uid).child(leave_type).update(c)
        if leave_type == "sick":
            try:
                try:
                    from_date = datetime.strptime(request.POST['fromdate'], '%Y-%m-%d')
                    to_date = datetime.strptime(request.POST['todate'], '%Y-%m-%d')
                   
                    reason = request.POST['reason']
                    c = {
                        "dep": dep,
                        "name": name,
                        "reason": reason,
                        "status": "Pending",
                        "node":"Full Day",
                    }

                    date_list = []

                    while from_date <= to_date:
                        date_list.append(from_date.strftime('%Y-%m-%d'))
                        from_date += timedelta(days=1)

                    for date in date_list:
                        year, month, day = map(int, date.split('-'))
                        c["date"] = date

                        if from_date == to_date:
                            db.child("leave_details").child(year).child(month).child(date).child(uid).child(leave_type).update(c)
                        else:
                            db.child("leave_details").child(year).child(month).child(date).child(uid).child(leave_type).update(c)
                except:
                    from_date = datetime.strptime(request.POST['fromdate'], '%Y-%m-%d') 
                    year, month, day = map(int, from_date.split('-'))
                    reason = request.POST['reason']
                    c = {
                        "dep": dep,
                        "name": name,
                        "reason": reason,
                        "status": "Pending",
                        "node":"Full Day",
                        "date":from_date,
                    }

                    
                    db.child("leave_details").child(year).child(month).child(from_date).child(uid).child(leave_type).update(c)    
            except:
                half_date = (request.POST.get('halfdate'))       
                reason = request.POST.get('reason')
                year, month, day = map(int, half_date.split('-'))

                c = {
                    "dep": dep,
                    "name": name,
                    "reason": reason,
                    "status": "Pending",
                    "node":"Half Day",
                    "date":half_date,
                }
                db.child("leave_details").child(year).child(month).child(half_date).child(uid).child(leave_type).update(c) 


        if leave_type == "permission":   
            fromtime = request.POST.get('starttime')  
            totime = request.POST.get('endtime')  
            reason = request.POST.get('reason')
            print("time",fromtime,totime,reason)
            if fromtime is not None and totime is not None:
                fromtiming = datetime.strptime(fromtime, "%H:%M")
                totiming = datetime.strptime(totime, "%H:%M")
                duration = totiming - fromtiming
                duration_hours, duration_minutes = divmod(duration.seconds, 3600)
                duration_str = '{:02}:{:02}'.format(duration_hours, duration_minutes)
                print("time", fromtime, totime, duration_str)
            else:
                print("From time and/or to time not provided.")
            
            c = {
                    "dep": dep,
                    "name": name,
                    "reason": reason,
                    "status": "Pending",
                    "date":current_date,
                    "duration": duration_str,
                }
            db.child("leave_details").child(current_year).child(current_month).child(current_date).child(uid).child(leave_type).update(c) 

    try:
        leavedata = db.child("leave_details").child(current_year).get().val()
        datelist,reasonlist,statelist,inchargelist=[],[],[],[]
        for monthdata in leavedata:
            for datedata in leavedata[monthdata]:
                print(datedata)
                try:
                    for leavetype in leavedata[monthdata][datedata][uid]:
                        datelist.append(leavedata[monthdata][datedata][uid][leavetype]["date"])
                        reasonlist.append(leavedata[monthdata][datedata][uid][leavetype]["reason"])
                        statelist.append(leavedata[monthdata][datedata][uid][leavetype]["status"])
                        try:
                            inchargelist.append(leavedata[monthdata][datedata][uid][leavetype]["updated_by"])
                        except:
                            inchargelist.append(False)
                except:
                    pass            

        print(datelist,reasonlist,statelist,inchargelist)
        leavehistory = zip(datelist,reasonlist,statelist,inchargelist)
        context = {
            "leavehistory": leavehistory,
            "dep":dep,
            "name":name,
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
            "suggestionNotification":suggestionNotification  
        }
        return render(request,'leave-form.html',context)
    except:
        pass
    return render(request,'leave-form.html')

def approvalprocess(request):
    uid1 = request.COOKIES["uid"]
    data = db.child("leave_details").get().val()
    name1 = checkUserName(uid1)
    if "approve" in request.POST:
        name = request.POST["namee1"]
        date = request.POST["_datee"]
        type = request.POST["type"]
        uid = getUidByName(name)
        db.child("leave_details").child(date[0:4]).child(date[5:7]).child(date).child(uid).child(type).update({"status": "Approved","updated_by":name1})

    if "deny" in request.POST:
        name = request.POST["namee1"]
        date = request.POST["_datee"]
        type = request.POST["type"]
        uid = getUidByName(name)
        db.child("leave_details").child(date[0:4]).child(date[5:7]).child(date).child(uid).child(type).update({"status": "Declined","updated_by":name1})
    return redirect('/leaveapproval/')


def late_form(request):
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

    loginState = request.COOKIES["loginState"]
    form_submitted = False
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
    todayDate = str(date.today())
    thisYear = datetime.now().strftime("%Y")
    thisMonth = datetime.now().strftime("%m")
    # istl = False
    # accounts = False
    # itaproval = False
    # rndaproval = False
    # praproval = False
    # aiaccess = False
    # tl = db.child("tl").get().val()
    # for t in tl:
    #     if name == tl[t]:
    #         istl = True
    #         break
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" or uid == 'Vhbt8jIAfiaV1HxuWERLqJh7dbj2':
    #     accounts = True

    # if  uid == 'jDYzpwcpv3akKaoDL9N4mllsGCs2':
    #     itaproval = True

    # if  uid == 'pztngdZPCPQrEvmI37b3gf3w33d2':
    #     rndaproval = True
    # if  uid == 'tQYuqy2ma6ecGURWSMpmNeVCHiD2' or uid == 'yleZdWDZgFYTBxwzC5NtHVeb3733':
    #     praproval = True 
    # if  uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
    #     aiaccess = True            

    if bool(loginState) == True:
        todayDate = str(date.today())
        thisYear = datetime.now().strftime("%Y")
        thisMonth = datetime.now().strftime("%m")
        if request.method == "POST":
            sd = request.POST["selectdate"]
            ft = request.POST["fromtime"]
            tt = request.POST["totime"]
            wd = request.POST["workdone"]
            wp = request.POST["workpercent"]
            reason = request.POST["reason"]
            if ft > tt:
                tdelta = datetime.strptime(tt, "%H:%M") - datetime.strptime(ft, "%H:%M")
                t = tdelta - timedelta(days=-1)
            else:
                tdelta = datetime.strptime(tt, "%H:%M") - datetime.strptime(ft, "%H:%M")
                t = tdelta - timedelta(days=0)
            timeinhrs = str(t)
            selectedYear = sd[0:4]
            selectedMonth = sd[5:7]
            selectedDate = sd[8:10]
            form_submitted = True

            context = {
                "from": ft,
                "to": tt,
                "name": checkUserName(uid),
                "time_in_hours": timeinhrs,
                "workDone": wd,
                "workPercentage": wp,
                "reason": reason,
                # "aiaccess":aiaccess
            }
            childName = ft + " to " + tt
            db.child("workmanager").child(selectedYear).child(selectedMonth).child(sd).child(uid).child("LateEntry").child(childName).set(context)
    context={
            "form_submitted": form_submitted,
            "dep":dep,"name":name,
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
            "suggestionNotification":suggestionNotification 
            }        
    return render(request, 'late_form.html',context)

def late_approval(request):
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
    # istl = False
    # accounts = False
    # suggestionNotification = 0
    # suggestionData = db.child("suggestion").get().val()
    # for suggestion in suggestionData:
    #         if not suggestionData[suggestion]["isread"]:
    #             suggestionNotification += 1
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" :
    #     accounts = True
    # management = False
    # if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2" or uid == '7lunH9jV0sV5EE2YzjjBrQWyVk72' or uid=="6WHjHuUai5ZimnLz4URUDssaMWj1":
    #          management = True   

    # tl = db.child("tl").get().val()
    # for t in tl:
    #     if name == tl[t]:
    #         istl = True
    #         break
    # data = db.child("staff").get().val()
    yearList, monthList, dateList, lateList = [], [], [], []
    # todayDate = str(date.today())
    # thisYear = datetime.now().strftime("%Y")
    # thisMonth = datetime.now().strftime("%m")
    data = db.child("workmanager").get().val()
    staff_data = db.child("staff").get().val()
    for staff in staff_data:
        for allYears in data:
            years = data[allYears]
            for allMonths in years:
                months = data[allYears][allMonths]
                for allDates in months:
                    try:
                        le = data[allYears][allMonths][allDates][staff]["LateEntry"]
                        for l in le:
                            lateDetails = le[l]
                            yearList.append(allYears)
                            monthList.append(allMonths)
                            dateList.append(allDates)
                            lateList.append(lateDetails)
                    except:
                        pass
    allList = zip(yearList, monthList, dateList, lateList)
    allListMobile = zip(yearList, monthList, dateList, lateList)
    context = {
        "name":name,
        "allList": allList,
        "allListMobile": allListMobile,
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
        "suggestionNotification":suggestionNotification  
    }
    return render(request,'lateapproval.html', context)

def leave_approval(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile=request.COOKIES["profile"]
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
    leavedata = db.child("leave_details").get().val()
    staff_data = db.child("staff").get().val()
    yearList, monthList, dateList, typelist, datalist = [], [], [], [], []
    for staff in staff_data:
        for allYears in leavedata:
            years = leavedata[allYears]
            for allMonths in years:
                months = leavedata[allYears][allMonths]
                for allDates in months:
                    try:
                        le = leavedata[allYears][allMonths][allDates][staff]
                        
                        for leave_type, leave_info in le.items():
                            types = leave_type
                            data = leave_info
                            yearList.append(allYears)
                            monthList.append(allMonths)
                            dateList.append(allDates)
                            typelist.append(types)
                            datalist.append(data)
                    except:
                        pass
        
    allList = zip(yearList, monthList, dateList, typelist, datalist)
    allListMobile = zip(yearList, monthList, dateList, typelist, datalist)
    context = {
        "leaveList": allList,
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
        "suggestionNotification":suggestionNotification  
    }
    return render(request,'approval.html', context)

def approval(request):
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
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
    leavedata = db.child("leave_details").get().val()
    staff_data = db.child("staff").get().val()
    yearList, monthList, dateList, typelist, datalist = [], [], [], [], []
    for staff in staff_data:
        for allYears in leavedata:
            years = leavedata[allYears]
            for allMonths in years:
                months = leavedata[allYears][allMonths]
                for allDates in months:
                    try:
                        le = leavedata[allYears][allMonths][allDates][staff]
                        
                        for leave_type, leave_info in le.items():
                            types = leave_type
                            data = leave_info
                            yearList.append(allYears)
                            monthList.append(allMonths)
                            dateList.append(allDates)
                            typelist.append(types)
                            datalist.append(data)
                    except:
                        pass
        
    allList = zip(yearList, monthList, dateList, typelist, datalist)

        
    context={
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
            "leaveList": allList,
            "suggestionNotification":suggestionNotification
    }    
    return render(request,'approval.html',context)

def submitaction(request):
    _year = request.POST["_year"]
    _month = request.POST["_month"]
    _date = request.POST["_date"]
    _from = request.POST["_from"]
    _to = request.POST["_to"]
    _name = request.POST["_name"]
    _reason = request.POST["_reason"]
    _time_in_hours = request.POST["_time_in_hours"]
    _workDone = request.POST["_workDone"]
    _workPercentage = request.POST["_workPercentage"] + " %"
    uid = getUidByName(_name)

    childName = _from + " to " + _to
    context = {
        "from": _from,
        "to": _to,
        "workDone": _workDone,
        "workPercentage": _workPercentage,
        "time_in_hours": _time_in_hours,
        "name": _name,
    }
    if "approved" in request.POST:
        db.child("workmanager").child(_year).child(_month).child(_date).child(uid).child(childName).set(context)
        db.child("workmanager").child(_year).child(_month).child(_date).child(uid).child("LateEntry").child(childName).remove()

    if "declined" in request.POST:
        db.child("workmanager").child(_year).child(_month).child(_date).child(uid).child("LateEntry").child(childName).remove()

    return redirect('/lateapproval/')


 
def suggestion(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile=request.COOKIES["profile"]
    current_date = datetime.now()
    general=False
    if uid is not None:
        general=True
    formatted_date = current_date.strftime("%Y-%m-%d")

    # Get the current year, month, and day
    current_year = str(current_date.year)
    current_month = str(current_date.month).zfill(2)
    current_day = str(current_date.day).zfill(2)   
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
    context = {
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
        "suggestionNotification":suggestionNotification
    }
    if request.method == "POST":
        msg = request.POST['msg']
        tm = datetime.now()
        date_time = tm.strftime("%Y-%m-%d_%H:%M:%S")
        date = tm.strftime("%Y-%m-%d")
        time = tm.strftime("%H:%M")
        val = {
            "message":msg,
            "date": date,
            "time":time,
            "uid":uid,
            "isread":False
        }
        db.child('suggestion').child(date_time).update(val)
        context = {
            "msg":"Message sent successfully",
            "dep":dep,
            "name":name,
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
            "suggestionNotification":suggestionNotification
           
        }
        return render(request, 'suggestion.html', context)
    return render(request,'suggestion.html', context)

def financialpost(request):
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1
    tm = datetime.now()
    thisYear = tm.strftime("%Y")
    thisMonth = tm.strftime("%m")
    if "close" in request.POST:
            return redirect(financial)
    if request.method == "POST":
        if "expense" in request.POST:
            uid = request.COOKIES["uid"]
            productName = request.POST["product-name"]
            dateTime = request.POST["date-time"]
            PurchasedDate, PurchasedTime =  dateTime.split('T')
            PurchasedDate=str(PurchasedDate)
            Purchyear,purchmont,purchdate = PurchasedDate.split("-")
            amount = request.POST["amount"]
            service = request.POST["service"]
            forDept = request.POST["for-dept"]
            now = datetime.now()
            enteredDate = now.strftime("%Y-%m-%d")
            enteredTime = now.strftime("%H:%M:%S")
            enteredBy = checkUserName(uid)
            contex = {
                "ProductName": productName,
                "PurchasedDate": PurchasedDate,
                "PurchasedTime": PurchasedTime,
                "Amount": amount,
                "Service": service, 
                "PurchasedFor": forDept,
                "EnteredDate": enteredDate,
                "EnteredTime": enteredTime,
                "EnteredBy": enteredBy,
                "suggestionNotification":suggestionNotification
            }
            db.child('FinancialAnalyzing').child('Expense').child(thisYear).child(purchmont).child(PurchasedDate+'_'+PurchasedTime).update(contex)

        if "income" in request.POST:
            uid = request.COOKIES["uid"]
            productName = request.POST["product-name"]
            customerName = request.POST["customer-name"]
            dateTime = request.POST["date-time"]
            PaidDate, PaidTime =  dateTime.split('T')
            amount = request.POST["amount"]
            invoiceNumber = request.POST["invoice-number"]
            paymentMethod = request.POST["payment-method"]
            now = datetime.now()
            enteredDate = now.strftime("%Y-%m-%d")
            enteredTime = now.strftime("%H:%M:%S")
            enteredBy = checkUserName(uid)
            contex = {
                "ProductName": productName,
                "CustomerName": customerName,
                "PaidDate": PaidDate,
                "PaidTime": PaidTime,
                "Amount": amount,
                "InvoiceNumber": invoiceNumber,
                "PaymentMethod": paymentMethod,
                "EnteredDate": enteredDate,
                "EnteredTime": enteredTime,
                "EnteredBy": enteredBy,
                "suggestionNotification":suggestionNotification
            }
            db.child('FinancialAnalyzing').child('Income').child(thisYear).child(thisMonth).child(PaidDate+'_'+PaidTime).update(contex)

        if 'delete' in request.POST:
            if "fromExpense" in request.POST:
                print("inside delete")
                edata = db.child("FinancialAnalyzing").child("Expense").get().val()
                oProductName = request.POST["oProductName"]
                oPurchasedDate = request.POST["oPurchasedDate"]
                oPurchasedTime = request.POST["oPurchasedTime"]
                oAmount = request.POST["oAmount"]
                oEnteredBy = request.POST["oEnteredBy"]
                oEnteredDate = request.POST["oEnteredDate"]
                oEnteredTime = request.POST["oEnteredTime"]
                year, month = oPurchasedDate.split("-")[0], oPurchasedDate.split("-")[1]
                db.child("FinancialAnalyzing").child("Expense").child(year).child(month).child(oPurchasedDate+"_"+oPurchasedTime).remove()
                return redirect(financial)

        if "remove" in request.POST:
            edata = db.child("FinancialAnalyzing").child("Expense").get().val()
            oProductName = request.POST["dProductName"]
            oPurchasedDate = request.POST["dPurchasedDate"]
            oPurchasedTime = request.POST["dPurchasedTime"]
            oAmount = request.POST["dAmount"]
            oEnteredBy = request.POST["dEnteredBy"]
            oEnteredDate = request.POST["dEnteredDate"]
            oEnteredTime = request.POST["dEnteredTime"]
            year, month = oPurchasedDate.split("-")[0], oPurchasedDate.split("-")[1]
            # try:
            #     edita = edata[year][month][oPurchasedDate+"_"+oPurchasedTime]
            # except Exception as e:
            #     edita = edata[year][month][oEnteredDate + "_" + oEnteredTime]
            db.child("FinancialAnalyzing").child("Expense").child(year).child(month).child(oPurchasedDate+"_"+oPurchasedTime).remove()

    
    return redirect(financial)

def financial(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile=request.COOKIES["profile"]
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
    tm = datetime.now()
    thisYear = tm.strftime("%Y")
    thisMonth = tm.strftime("%m")
    
    if request.method == "POST":
        date = request.POST["get-total"]
        thisyear=date[0:4]
        thismonth=date[5:7]
        incomeList, expenseList = [], []
        incomeData, expenseData = False, False
        expenseamount, incomeamount, salary = 0, 0, 0

        try:
            try:
                ed = db.child("FinancialAnalyzing").child("Expense").get().val()
            except:
                pass
            try:
                id = db.child("FinancialAnalyzing").child("Income").get().val()
            except:
                pass
            try:
                for f in id[thisyear][thismonth]:
                    incomeList.append(id[thisyear][thismonth][f])
                    incomeData = True
                    incomeamount += int(id[thisyear][thismonth][f]["Amount"])
            except:
                pass
            try:
                for f in ed[thisyear][thismonth]:
                    expenseList.append(ed[thisyear][thismonth][f])
                    expenseData = True
                    expenseamount += int(ed[thisyear][thismonth][f]["Amount"])
                    if (ed[thisyear][thismonth][f]["Service"]).lower() == "salary":
                        salary = int(ed[thisyear][thismonth][f]["Amount"])
            except:
                pass
        except:
            pass
        if expenseamount>incomeamount:
            diffWithSalary = expenseamount - incomeamount
            color = "Red"
        else:
            diffWithSalary = incomeamount - expenseamount
            color = "Green"
        expenseWithoutSalary = expenseamount - salary
        if expenseWithoutSalary>incomeamount:
            diffWithoutSalary = expenseWithoutSalary - incomeamount
            dcolor = "Red"
        else:
            diffWithoutSalary = incomeamount - expenseWithoutSalary
            dcolor = "Green"
        context = {
            "name":name,
            "dep":dep,
            "profile":profile,
            "incomeList": incomeList,
            "expenseList": expenseList,
            "incomeData": incomeData,
            "incomeamount": incomeamount,
            "expenseData": expenseData,
            "expenseamount": expenseamount,
            "expenseWithoutSalary": expenseWithoutSalary,
            "diffWithSalary": diffWithSalary,
            "diffWithoutSalary": diffWithoutSalary,
            "color": color,
            "dcolor": dcolor,
            "date": thismonth+"-"+thisyear,
            "dep": dep,
            "suggestionNotification":suggestionNotification,
            "container": True,
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
        return render(request, "financial.html", context)
      
    incomeList, expenseList = [], []
    incomeData, expenseData = False, False
    expenseamount, incomeamount, salary = 0, 0, 0
    try:
        try:
            ed = db.child("FinancialAnalyzing").child("Expense").get().val()
        except:
            pass
        try:
            id = db.child("FinancialAnalyzing").child("Income").get().val()
        except:
            pass
        try:
            for _year in id:
                for _month in id[_year]:
                    try:
                        for f in id[_year][_month]:
                            mm = (id[_year][_month][f]["PaidDate"]).split("-")[1]
                            # print(mm)
                            if thisMonth == mm:
                                incomeList.append(id[_year][_month][f])
                                incomeData = True
                                # incomeamount += int(id[_year][_month][f]["Amount"])
                                incomeamount += int(id[_year][_month][f]["Amount"].replace(',', ''))
                    except Exception as e:
                       pass
        except:
            pass
        salary = 0
        try:
            for _year in ed:
                for _month in ed[_year]:
                    for f in ed[_year][_month]:
                        mm = (ed[_year][_month][f]["PurchasedDate"]).split("-")[1]
                        if thisMonth == mm:
                            expenseList.append(ed[_year][_month][f])
                            expenseData = True
                            expenseamount += int(ed[_year][_month][f]["Amount"])
                            service = ed[_year][_month][f]["Service"]
                            if str(service).lower() == "salary":
                                salary += int(ed[_year][_month][f]["Amount"])
        except:
            pass
    except:
        pass
    if expenseamount>incomeamount:
        diffWithSalary = expenseamount - incomeamount
        color = "Red"
    else:
        diffWithSalary = incomeamount - expenseamount
        color = "Green"
    expenseWithoutSalary = expenseamount - salary
    if expenseWithoutSalary>incomeamount:
        diffWithoutSalary = expenseWithoutSalary - incomeamount
        dcolor = "Red"
    else:
        diffWithoutSalary = incomeamount - expenseWithoutSalary
        dcolor = "Green"
    context = {
        "name":name,
        "dep":dep,
        "profile":profile,
        "incomeList": incomeList,
        "expenseList": expenseList,
        "incomeData": incomeData,
        "incomeamount": incomeamount,
        "expenseData": expenseData,
        "expenseamount": expenseamount,
        "expenseWithoutSalary": expenseWithoutSalary,
        "diffWithSalary": diffWithSalary,
        "diffWithoutSalary": diffWithoutSalary,
        "color": color,
        "dcolor": dcolor,
        "date": thisMonth+"-"+thisYear,
        "dep": dep,
        "suggestionNotification":suggestionNotification,
        "container": True,
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
    return render(request, "financial.html", context)

def inventorymanagement(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile=request.COOKIES["profile"]
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
    allDataBase = db.get().val()
    editvalue=[]
    if 'getid1' in request.POST:
        inventory = allDataBase["inventory_management"]
        getid=request.POST['getid']
        editvalue.append(inventory[getid])

    if 'getid2' in request.POST:
        getid=request.POST['getid']
        db.child("inventory_management").child(getid).remove()

    if 'update' in request.POST:
        id=request.POST['id']
        max_price=request.POST['max_price']
        min_price=request.POST['min_price']
        name=request.POST['name']
        obc=request.POST['obc']
        stock=request.POST['stock']

        data={
            "id":id,
            "max_price":max_price,
            "min_price":min_price,
            "name":name,
            "obc":obc,
            "stock":stock
        }
        db.child("inventory_management").child(id).update(data)

    allDataBase = db.get().val()
    inventory = allDataBase["inventory_management"]
    inventorylist=[]
    snolist=[]
    sno=0
    for id in inventory:
        inventorylist.append(inventory[id])
        sno=sno+1
        snolist.append(sno)
    allinventory=zip(snolist,inventorylist)    
    inventorylist2=[]
    snolist=[]
    sno=0
    for id in inventory:
        inventorylist2.append(inventory[id])
        sno=sno+1
        snolist.append(sno)  
    context={
        "editvalue":editvalue,
        "allinventory":allinventory,
        "dep": dep,
        "name":name,
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
        "suggestionNotification":suggestionNotification
    }
    return render(request,'inventorymanagement.html',context)

def coohome(request):
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
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
    installation = db.child("Installationdetails").get().val()
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")

    # Get the current year, month, and day
    current_year = str(current_date.year)
    current_month = str(current_date.month).zfill(2)
    current_day = str(current_date.day).zfill(2)

    # Calculate yesterday's date
    yesterday = current_date - timedelta(days=1)

    # Get yesterday's year, month, and day
    yesterday_year = str(yesterday.year)
    yesterday_month = str(yesterday.month).zfill(2)
    yesterday_day = str(yesterday.day).zfill(2)

    saturday_date = yesterday - timedelta(days=1)
    saturday_year = str(saturday_date.year)
    saturday_month = str(saturday_date.month).zfill(2)
    saturday_day = str(saturday_date.day).zfill(2)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    current_date = datetime.now()
    selected_year = current_date.strftime('%Y')
    selected_month = current_date.strftime("%m")
    current_date1 = datetime.now().strftime("%d")
    attendence = db.child("attendance").get().val()
    alllist=[]
    alldates = installation[selected_year][selected_month]
    for date in alldates:
        alluid = installation[selected_year][selected_month][date]
        date_object = datetime.strptime(date, '%Y-%m-%d')

            # Check if the date is within the last 7 days
        if start_date <= date_object <= end_date:
            for num, data in alluid.items():
                alllist.append((num, data)) 
    inventory=db.child("inventory_management").get().val()
    inventoryall=[]
    for uid1 in inventory:
        inventoryall.append(inventory[uid1]) 

    try:
        try:
            print("==")
            print("date", current_year, current_month, current_day, uid)
            todaycheckin = attendence[current_year][current_month][current_day][uid]["check_in"]
            
            print("today", todaycheckin)
        except:
            todaycheckin = "No Entry"

        try:
            todaycheckout = attendence[current_year][current_month][current_day][uid]["check_out"]
            
        except:
            todaycheckout = "No Entry"
        day = False
        try:
            if yesterday.weekday() == 6:
                yescheckin = attendence[saturday_year][saturday_month][saturday_day][uid]["check_in"]
                day = "Saturday"
                yesscheckin = convert_to_12_hour_format(yescheckin)
            else:
                # If yesterday was not a Sunday, use the existing code for Sunday data
                yescheckin = attendence[yesterday_year][yesterday_month][yesterday_day][uid]["check_in"]
                yesscheckin = convert_to_12_hour_format(yescheckin)
                day = False
        except:
            yesscheckin = "No Entry"

        try:
            if yesterday.weekday() == 6:
                yescheckout = attendence[saturday_year][saturday_month][saturday_day][uid]["check_out"]
                yesscheckout = convert_to_12_hour_format(yescheckout)
            else:    
                yescheckout = attendence[yesterday_year][yesterday_month][yesterday_day][uid]["check_out"]
                yesscheckout = convert_to_12_hour_format(yescheckout)
        except:
            yesscheckout = "No Entry"

        try:
            if yesterday.weekday() == 6:
                yesprogress = attendence[saturday_year][saturday_month][saturday_day][uid]["working_hours"]
                yesterdayprogress = calculate_progress(yesprogress)
            else:    
                yesprogress = attendence[yesterday_year][yesterday_month][yesterday_day][uid]["working_hours"]
                yesterdayprogress = calculate_progress(yesprogress)
                print("progress", yesterdayprogress)
        except:
            yesterdayprogress = "Absent"    
        try:
            today_progress= calculate_progress_(todaycheckin, todaycheckout)
            print("prog",today_progress)
        except:
            today_progress= "Absent"
        todaycheckout = convert_to_12_hour_format(todaycheckout)
        todaycheckin = convert_to_12_hour_format(todaycheckin)   
    except:
        pass
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
    context={
        "alllist":alllist,
        "inventoryall":inventoryall,
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
        "suggestionNotification":suggestionNotification,
        "todaycheckin": todaycheckin,
        "todaycheckout": todaycheckout,
        "yescheckin": yesscheckin,
        "yescheckout": yesscheckout,
        "yesprogress":yesterdayprogress,
        "todayprogress":today_progress,
        "day":day
    }    
    return render(request,'coohome.html',context)

def installation_details(request):
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
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
    installation = db.child("Installationdetails").get().val()
    if request.method == "POST":
        if "delete_entry" in request.POST:
            print("==")
            num_to_delete = request.POST.get("delete_num")
            date_to_delete = request.POST.get("delete_date")
            print("num",num_to_delete,date_to_delete)
            date_parts = date_to_delete.split("-")
            tyear = date_parts[0]
            tmonth = date_parts[1]
            print("year",tyear,tmonth)
            db.child("Installationdetails").child(tyear).child(tmonth).child(date_to_delete).child(num_to_delete).remove()
            # installation[tyear][tmonth][date_to_delete].remove(num_to_delete)

            return HttpResponseRedirect('/installation_details/')
        selected_month = request.POST.get("get-total")
        # Split the selected_month into year and month parts
        selected_year, selected_month = selected_month.split("-")
    else:
        current_date = datetime.now()
        selected_year = current_date.strftime('%Y')
        selected_month = current_date.strftime("%m")
    alllist=[]
    alldates = installation[selected_year][selected_month]
    for date in alldates:
        alluid = installation[selected_year][selected_month][date]
        for num, data in alluid.items():
            alllist.append((num, data))       
    context={
        "alllist":alllist,
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
        "suggestionNotification":suggestionNotification
    }
    return render(request,'installation_details.html',context)

def todo(request):
    return render(request,'todo.html')
def workdonedetails(request):
    # todaysDate = str(date.today())
    # day = (date.today()).strftime("%A")
    # _year = todaysDate[:4]
    # _month = todaysDate[5:7]
    # workDoneListFinal = []
    # workDoneListFinal.clear()
    # uid = request.COOKIES["uid"]
    # dep = request.COOKIES["dep"]
    # name = checkUserName(uid)
    # istl = False
    # accounts = False
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
    #     accounts = True
    # management = False
    # if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2":
    #          management = True      
    # data = db.child("staff").get().val()
    # fingerprintData = db.child("fingerPrint").get().val()
    # if request.method == "POST":
    #     dep = request.POST['dep']
    #     dte = request.POST['dte']
    #     if dep == "IT":
    #         if not dte:
    #             dte = str(datetime.today().date())
    #         ddte = datetime.strptime(dte, '%Y-%m-%d').date()
    #         day = ddte.strftime("%A")
    #         _year, _month, todaysDate = dte[0:4], dte[5:7], dte
    #         totalName, totalTime, punchingTime = [], [], []
    #         for x in data:
    #             mysum = timedelta()
    #             if data[x]['department'] == "MEDIA":
    #                 try:
    #                     _todaysDateData = data[x]["workManager"]["timeSheet"][_year][_month][todaysDate]
    #                     for _time in _todaysDateData:
    #                         try:
    #                             if _todaysDateData[_time]["time_in_hours"]:
    #                                 workDoneListFinal.append(_todaysDateData[_time])
    #                             tm = _todaysDateData[_time]['time_in_hours']
    #                             if len(tm)>5:
    #                                 (h, m, s) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    #                             else:
    #                                 (h, m) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m))
    #                             mysum += d
    #                         except:
    #                             pass
    #                     try:
    #                         fd = fingerprintData[x][todaysDate]
    #                         for f in fd:
    #                             f = convert24HoursTime(f)
    #                             punchingTime.append(f)
    #                             break
    #                     except:
    #                         punchingTime.append('Entry Not Registered')

    #                     totalName.append(data[x]['name'])
    #                     totalTime.append(mysum)
    #                 except:
    #                     pass
    #             if data[x]['department'] == "APP":
    #                 try:
    #                     _todaysDateData = data[x]["workManager"]["timeSheet"][_year][_month][todaysDate]
    #                     for _time in _todaysDateData:
    #                         try:
    #                             if _todaysDateData[_time]["time_in_hours"]:
    #                                 workDoneListFinal.append(_todaysDateData[_time])
    #                             tm = _todaysDateData[_time]['time_in_hours']
    #                             if len(tm)>5:
    #                                 (h, m, s) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    #                             else:
    #                                 (h, m) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m))
    #                             mysum += d
    #                         except:
    #                             pass
    #                     try:
    #                         fd = fingerprintData[x][todaysDate]
    #                         for f in fd:
    #                             f = convert24HoursTime(f)
    #                             punchingTime.append(f)
    #                             break
    #                     except:
    #                         punchingTime.append('Entry Not Registered')

    #                     totalName.append(data[x]['name'])
    #                     totalTime.append(mysum)
    #                 except:
    #                     pass
    #             if data[x]['department'] == "WEB":
    #                 try:
    #                     _todaysDateData = data[x]["workManager"]["timeSheet"][_year][_month][todaysDate]
    #                     for _time in _todaysDateData:
    #                         try:
    #                             if _todaysDateData[_time]["time_in_hours"]:
    #                                 workDoneListFinal.append(_todaysDateData[_time])
    #                             tm = _todaysDateData[_time]['time_in_hours']
    #                             if len(tm)>5:
    #                                 (h, m, s) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    #                             else:
    #                                 (h, m) = tm.split(':')
    #                                 d = timedelta(hours=int(h), minutes=int(m))
    #                             mysum += d
    #                         except:
    #                             pass
    #                     try:
    #                         fd = fingerprintData[x][todaysDate]
    #                         for f in fd:
    #                             f = convert24HoursTime(f)
    #                             punchingTime.append(f)
    #                             break
    #                     except:
    #                         punchingTime.append('Entry Not Registered')

    #                     totalName.append(data[x]['name'])
    #                     totalTime.append(mysum)
    #                 except:
    #                     pass
    #         combined = list(zip(totalName, totalTime, punchingTime))
    #         combined.sort(key=lambda x: x[1])
    #         # totalName, totalTime, punchingTime = zip(*combined)
    #         total = zip(totalName, totalTime, punchingTime)
    #         context = {
    #             "dep":dep,
    #             "day":day,
    #             "date": todaysDate,
    #             "firstTable": workDoneListFinal,
    #             "total": total,
    #             "tl":getTl(dep),
    #             "tl":istl,
    #             "accounts":accounts,
    #             "dep":dep,
    #             "management":management
    #         }
    return render (request,'workdonedetails.html')

def refreshment(request):
    print("refreshment")
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
    if request.method == "POST":
        todayDate = str(date.today())
        currTime = datetime.now().strftime("%H:%M")
        selected_refreshments = request.POST.getlist("refreshment")
        d = db.child("refreshments").get().val()
        uid = request.COOKIES["uid"]
        _name = checkUserName(uid)
        dep = checkUserDepartment(uid)
        for choosen in selected_refreshments:
            if choosen == "tea":
                if currTime < "14:00":
                    try:
                        d[todayDate]["FN"][choosen]
                        a = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                if currTime > "14:00":
                    try:
                        d[todayDate]["AN"][choosen]
                        a = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
            if choosen == "coffee":
                if currTime < "14:00":
                    try:
                        d[todayDate]["FN"][choosen]
                        a = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                if currTime > "14:00":
                    try:
                        d[todayDate]["AN"][choosen]
                        a = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
            if choosen == "milk":
                if currTime < "14:00":
                    try:
                        d[todayDate]["FN"][choosen]
                        a = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("FN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["FN"][choosen])
                        db.child("refreshments").child(todayDate).child("FN").update({choosen + "_count": newLen})
                if currTime > "14:00":
                    try:
                        d[todayDate]["AN"][choosen]
                        a = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("AN").child(choosen).update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate]["AN"][choosen])
                        db.child("refreshments").child(todayDate).child("AN").update({choosen + "_count": newLen})
            
    
            if choosen == "Lunch":
                if currTime < "14:00":
                    try:
                        d[todayDate][choosen]["lunch_list"]
                        a = len(d[todayDate][choosen]["lunch_list"])
                        db.child("refreshments").child(todayDate).child("Lunch").child("lunch_list").update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate][choosen]["lunch_list"])
                        db.child("refreshments").child(todayDate).child("Lunch").update({choosen + "_count": newLen})
                    except:
                        db.child("refreshments").child(todayDate).child("Lunch").child("lunch_list").update({"name1": _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate][choosen]["lunch_list"])
                        db.child("refreshments").child(todayDate).child("Lunch").update({choosen + "_count": newLen})
        if uid == "pztngdZPCPQrEvmI37b3gf3w33d2":
            return redirect('coohome')
        if uid == "A5kpLL2U0UaOkPrw2GeI8llH49s1" or uid == "yleZdWDZgFYTBxwzC5NtHVeb3733" or uid== "jDYzpwcpv3akKaoDL9N4mllsGCs2":
            return redirect('adminhome')
        if dep == "APP":
            return redirect('ithome')
        if dep == "WEB":
            return redirect('ithome')
        if dep == "MEDIA":
            return redirect('ithome')
        if dep == "PR":
            return redirect("prhome")
        if dep == "RND":
            return redirect("rndhome")
        if dep == "ADMIN":
            return redirect("adminhome")
        if dep == "Installation":
            return redirect("rndhome")
        if dep == "AIML":
            return redirect("ithome")
        if dep == "HR":
            return redirect("hrhome")
        
            
    
def submitwork(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    
    loginState = request.COOKIES["loginState"]
    if bool(loginState) == True:
        todayDate = str(date.today())
        thisYear = datetime.now().strftime("%Y")
        thisMonth = datetime.now().strftime("%m")
        if request.method == "POST" and "percent" in request.POST:
            fromTime = request.POST["from-time"]
            toTime = request.POST["to-time"]
            _percent = request.POST["percent"] + "%"
            wd = request.POST["workdone"]
            try:
                awd = request.POST["addedworkdone"]
                wd = wd + " and " + awd
            except:
                pass

            if fromTime > toTime:
                tdelta = datetime.strptime(toTime, "%H:%M") - datetime.strptime(fromTime, "%H:%M")
                t = tdelta - timedelta(days=-1)
            else:
                tdelta = datetime.strptime(toTime, "%H:%M") - datetime.strptime(fromTime, "%H:%M")
                t = tdelta - timedelta(days=0)
            timeinhrs = str(t)
            context = {
                "from": fromTime,
                "to": toTime,
                "name": checkUserName(uid),
                "time_in_hours": timeinhrs,
                "workDone": wd,
                "workPercentage": _percent,
            }
            childName = fromTime + " to " + toTime
            if fromTime == "" or toTime == "":
                pass
            else:
                db.child("workmanager").child(thisYear).child(thisMonth).child(todayDate).child(uid).child(childName).set(context)
        if dep == "APP":
            return redirect('ithome')
        if dep == "WEB":
            return redirect('ithome')
        if dep == "MEDIA":
            return redirect('ithome')
        if dep == "PR":
            return redirect("prhome")
        if dep == "RND":
            return redirect("rndhome")
        if dep == "ADMIN":
            return redirect("adminhome")
        if dep == "Installation":
            return redirect("rndhome")
        if dep == "AIML":
            return redirect("ithome")
        if dep == "HR":
            return redirect("hrhome")  

def editworkdone(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
    loginState = request.COOKIES["loginState"]
    if bool(loginState) == True:
        todayDate = str(date.today())
        thisYear = datetime.now().strftime("%Y")
        thisMonth = datetime.now().strftime("%m")
        if request.method == "POST":
            fromTime = request.POST["from-time"]
            toTime = request.POST["to-time"]
            _percent = request.POST["percent"] + "%"
            wd = request.POST["workdone"]
            default_from_time=request.POST["default_fromtime"]
            default_to_time=request.POST["default_totime"]
            try:
                awd = request.POST["addedworkdone"]
                wd = wd + " and " + awd
            except:
                pass

            if fromTime > toTime:
                tdelta = datetime.strptime(toTime, "%H:%M") - datetime.strptime(fromTime, "%H:%M")
                t = tdelta - timedelta(days=-1)
            else:
                tdelta = datetime.strptime(toTime, "%H:%M") - datetime.strptime(fromTime, "%H:%M")
                t = tdelta - timedelta(days=0)
            timeinhrs = str(t)
            context = {
                "from": fromTime,
                "to": toTime,
                "name": checkUserName(uid),
                "time_in_hours": timeinhrs,
                "workDone": wd,
                "workPercentage": _percent,
            }
            childName1 = default_from_time + " to " + default_to_time
            childName = fromTime + " to " + toTime
            if fromTime == "" or toTime == "":
                pass
            else:
                db.child("workmanager").child(thisYear).child(thisMonth).child(todayDate).child(uid).child(childName1).remove()
                db.child("workmanager").child(thisYear).child(thisMonth).child(todayDate).child(uid).child(childName).set(context)
        if dep == "APP":
            return redirect('ithome')
        if dep == "WEB":
            return redirect('ithome')
        if dep == "MEDIA":
            return redirect('ithome')
        if dep == "PR":
            return redirect("prhome")
        if dep == "RND":
            return redirect("rndhome")
        if dep == "ADMIN":
            return redirect("adminhome")
        if dep == "Installation":
            return redirect("rndhome")
        if dep == "AIML":
            return redirect("ithome")
        if dep == "HR":
            return redirect("hrhome") 

def checkUserDepartment(uid):
    data = db.child("staff").get().val()
    for x in data:
        if uid == x:
            dep = data[x]["department"]
            return dep

def checkUserName(uid):
    try:
        data = db.child("staff").get().val()
        if data:
            for x in data:
                if uid == x:
                    z = data[x]["name"]
                    return z
        else:
            print("No data found.")
    except Exception as e:
        print("An error occurred:", str(e))
    return None 

def getUidByName(name):
    data = db.child("staff").get().val()
    for x in data:
        if data[x]["name"] == name:
            return x

def logout(request):
    response = redirect("login")
    response.delete_cookie("uid")
    response.delete_cookie("loginState")
    return response            

def prdashboard(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
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
    if 'total-target' in request.POST:
        totalprgettarget=request.POST['totalprgettarget']
        totalprtarget=request.POST['totalprtarget']
        if totalprgettarget:
            db.child("PRDashboard").child("prtarget").update({"totalprgettarget":totalprgettarget})
        if totalprtarget:
            db.child("PRDashboard").child("prtarget").update({"totalprtarget":totalprtarget})
    dashboardDB = db.child("PRDashboard").get().val()
    totalprgettarget = dashboardDB["prtarget"]["totalprgettarget"]
    totalprtarget= dashboardDB["prtarget"]["totalprtarget"]
    namelist=[]
    uidlist=[]
    profilepic=[]
    try:
        staff_data = db.child("staff").get().val()
        if staff_data:
            for uid, data in staff_data.items():
                department = data.get("department")
                if department == "PR":
                    namelist.append(data.get("name"))
                    uidlist.append(uid)
                    profilepic.append(data.get("profileImage", None))
                else:
                    pass
    except Exception as e:
        print(f"An error occurred: {e}")

    if "employeeofmonth" in request.POST:
        selected_uid = request.POST.get("name")  
        reason = request.POST.get("reason")
        data_to_update = {
            "person": selected_uid,
            "reason": reason
        }
        try:
            db.child("PRDashboard").child("employee_of_week").update(data_to_update) 
           
        except:
            pass  

    if "progresssubmit" in request.POST:
        progress = request.POST['progress']
        if progress:
            db.child("PRDashboard").update({"progress": progress}) 
            
    dashboardDB = db.child("PRDashboard").get().val()
    progress1=dashboardDB["progress"]    


    dropdown=zip(namelist,uidlist,profilepic)
    context={
        "totalprgettarget":totalprgettarget,
        "totalprtarget":totalprtarget,
        "dep":dep,
        "name":name,
        "profile":profile,
        "dropdown":dropdown,
        "progress":progress1,
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
        "suggestionNotification":suggestionNotification
    }
    return render(request,'admindashboard.html',context)

def userdata(request):
    uid = request.COOKIES["uid"]
    name = request.COOKIES["name"]
    dep = request.COOKIES["dep"]
    profile=request.COOKIES["profile"]
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
    userdata = aidb.child("onyx").get().val()
    no_data_message = ""  
    default_data = {}  
    like_data = {} 
    dislike_data = {} 

    if request.method == 'POST':
        selected_date1 = request.POST.get('selected_date') 
        if selected_date1:
            selected_date = datetime.strptime(selected_date1, "%Y-%m-%d")

            selected_year = selected_date.strftime("%Y")
            selected_month = selected_date.strftime("%m")

            entry = userdata.get(selected_year, {}).get(selected_month, {}).get(selected_date1, {})

            categories = ["default", "dislike", "like"]

            if entry is not None:
                for category in categories:
                    try:
                        for did in entry[category]:
                            command = entry[category][did].get("command", "No command")
                            reply = entry[category][did].get("reply", "No Reply")

                            if category == "default":
                                default_data[did] = {"command": command, "reply": reply}
                            elif category == "like":
                                like_data[did] = {"command": command, "reply": reply}
                            elif category == "dislike":
                                dislike_data[did] = {"command": command, "reply": reply}
                    except KeyError:
                        pass
            else:
                no_data_message = "No data found for the selected date." 

    context = {
        "name":name,
        "dep":dep,
        "profile":profile,
        "default_data": default_data,
        "like_data": like_data,
        "dislike_data": dislike_data,
        "no_data_message": no_data_message,
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
        "suggestionNotification":suggestionNotification
    } 
    return render(request,'userdata.html',context)

def profileall(uid):
    profiledata=db.child("staff").get().val()
    try:
        profilepic=profiledata[uid]["profileImage"]
    except:
        profilepic="NULL"
    return profilepic  

def convert24HoursTime(time):
  if int(time[0:2]) > 12:
    x = int(time[0:2]) - 12
    y = str(x) + time[2:] + " PM"
    return y
  elif int(time[0:2]) == 12:
    y = time + " PM"
    return y
  else:
    y = time + " AM"
    return y

def getTl(dep):
    data = db.child('tl').get().val()
    for x in data:
        if x == dep:
            return data[x]    
        
def workmanagerTl(request):
    today=datetime.now().strftime("%Y-%m-%d")
    cur_day=datetime.now().strftime("%d")
    current_month=datetime.now().strftime("%m")
    current_year=datetime.now().strftime("%Y")
    workdetails=db.child("workmanager").child(current_year).child(current_month).child(today).get().val()
    staff=db.child("staff").get().val()
    # for uid in staff:
    #     if staff[uid]["department"] == "IT":
    #         try:
    #             for fulldata in workdetails[uid]:
                    
    #         except:
    #             pass      
    return render(request,'workmanagerTL.html')  
def  deleteaccess(request):
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
        if "deleteaccess" in request.POST:
            uid = request.POST["uid"]
            access = request.POST["removeaccess"]
            web=db.child("webaccess").child(access).get().val()
            for uid1 in web:
                if uid == web[uid1]:
                    data={
                        uid1:"removed"
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
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1
    context={
        "allstaff":allstaff,
        "allstaff1":allstaff,
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
        "suggestionNotification":suggestionNotification
    }
    return render(request,'deleteaccess.html')

def forgetpassword(request):
    return render(request,'deleteaccess.html')
def calculate_progress_(today_checkin, today_checkout, goal_hours=9):
    try:
        print("starting")
        asia_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(asia_timezone).strftime('%H:%M:%S')

        if today_checkin != "No Entry":
            today_checkin_time = datetime.strptime(today_checkin, "%H:%M:%S")
            
            if today_checkout == "No Entry":
                today_checkout_time = datetime.strptime(current_time, "%H:%M:%S")
            else:
                today_checkout_time = datetime.strptime(today_checkout, "%H:%M:%S")

            time_difference = today_checkout_time - today_checkin_time
            progress_hours = time_difference.total_seconds() / 3600
            progress_percentage = (progress_hours / goal_hours) * 100
            print("func",progress_percentage)

            return progress_percentage
        else:
            return "No Entry"
    except Exception as e:
        print(f"Error: {e}")
        return "No Entry"
   
def calculate_progress(working_hours, goal_hours=9):
    try:
        # Convert the working_hours to a timedelta object
        working_hours = datetime.strptime(working_hours, "%H:%M:%S").time()

        # Calculate the total working time in seconds
        total_working_seconds = working_hours.hour * 3600 + working_hours.minute * 60 + working_hours.second

        # Calculate progress as a percentage
        progress_percentage = min(100, (total_working_seconds / (goal_hours * 3600)) * 100)

        return progress_percentage
    except:
        return "Absent"    

def convert_to_12_hour_format(progress):
    try:
        time_24h_obj = datetime.strptime(progress, "%H:%M:%S")
        time_12h = time_24h_obj.strftime("%I:%M %p")
    except:
        time_12h = "No Entry"    
    return time_12h


   
    return render(request,'deleteaccess.html')   
