from django.shortcuts import render, redirect
import pyrebase, requests
from datetime import date, datetime, timedelta, time
from django.http import HttpResponse

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
                response = redirect("rndhome")
                return response
            if dep == "ADMIN":
                response = redirect("adminhome")
                return response
            if dep == "INSTALLATION":
                response = redirect("installationhome")
                return response
            if dep == "AIML":
                response = redirect("aimlhome")
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
            exp = 100 * 365 * 24 * 60 * 60
            if dep == "APP":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "WEB":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "MEDIA":
                response = redirect("ithome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "PR":
                print("log pr")
                response = redirect("prhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "RND":
                response = redirect("rndhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "ADMIN":
                response = redirect("adminhome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
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
    name = checkUserName(uid)
    leave_data = db.child("leaveDetails").get().val()
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")

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
                            db.child("leaveDetails").child(year).child(month).child(date).child(uid).child(leave_type).set(c)
                        else:
                            db.child("leaveDetails").child(year).child(month).child(date).child(uid).child(leave_type).set(c)
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

                  
                    db.child("leaveDetails").child(year).child(month).child(from_date).child(uid).child(leave_type).set(c)    
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
                db.child("leaveDetails").child(year).child(month).child(half_date).child(uid).child(leave_type).set(c)
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
                            db.child("leaveDetails").child(year).child(month).child(date).child(uid).child(leave_type).set(c)
                        else:
                            db.child("leaveDetails").child(year).child(month).child(date).child(uid).child(leave_type).set(c)
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

                    
                    db.child("leaveDetails").child(year).child(month).child(from_date).child(uid).child(leave_type).set(c)    
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
                db.child("leaveDetails").child(year).child(month).child(half_date).child(uid).child(leave_type).set(c) 


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
            db.child("leaveDetails").child(current_year).child(current_month).child(current_date).child(uid).child(leave_type).set(c) 

    try:
        print('test=============',uid)
        leavedata = db.child("leaveDetails").child(current_year).get().val()
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
            "name":name
            # "tl": istl,
            # "dep":dep,
            # "accounts":accounts,
            # "management":management,
            # "suggestionNotification":suggestionNotification
        }
        return render(request,'leave-form.html',context)
    except:
        pass
    return render(request,'leave-form.html')

def approvalprocess(request):
    uid1 = request.COOKIES["uid"]
    data = db.child("leaveDetails").get().val()
    name1 = checkUserName(uid1)
    if "approve" in request.POST:
        name = request.POST["namee1"]
        date = request.POST["_datee"]
        type = request.POST["type"]
        uid = getUidByName(name)
        db.child("leaveDetails").child(date[0:4]).child(date[5:7]).child(date).child(uid).child(type).update({"status": "Approved","updated_by":name1})

    if "deny" in request.POST:
        name = request.POST["namee1"]
        date = request.POST["_datee"]
        type = request.POST["type"]
        uid = getUidByName(name)
        db.child("leaveDetails").child(date[0:4]).child(date[5:7]).child(date).child(uid).child(type).update({"status": "Declined","updated_by":name1})
    return redirect('/leaveapproval/')


def late_form(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    loginState = request.COOKIES["loginState"]
    form_submitted = False
    name = checkUserName(uid)
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
            
    return render(request, 'late_form.html', {"form_submitted": form_submitted, "dep":dep,"name":name})

def late_approval(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
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
        # "tl": istl,
        "dep":dep,
        # "accounts":accounts,
        # "management":management,
        # "suggestionNotification":suggestionNotification
    }
    return render(request,'lateapproval.html', context)

def leave_approval(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    leavedata = db.child("leaveDetails").get().val()
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
        # "tl": istl,
        "dep":dep,
        # "accounts":accounts,
        # "management":management,
        # "suggestionNotification":suggestionNotification
    }
    return render(request,'approval.html', context)

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
    name = checkUserName(uid)
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")

    # Get the current year, month, and day
    current_year = str(current_date.year)
    current_month = str(current_date.month).zfill(2)
    current_day = str(current_date.day).zfill(2)
    # istl = False
    # itaproval = False
    # rndaproval = False
    # praproval = False
    # tl = db.child("tl").get().val()
    # for t in tl:
    #     if name == tl[t]:
    #         istl = True
    #         break
    # accounts = False
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
    #     accounts = True
    # management = False
    # if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2":
    #     management = True

    # if  uid == 'jDYzpwcpv3akKaoDL9N4mllsGCs2':
    #     itaproval = True

    # if  uid == 'pztngdZPCPQrEvmI37b3gf3w33d2' or uid =='Vhbt8jIAfiaV1HxuWERLqJh7dbj2':
    #     rndaproval = True
    # if  uid == 'tQYuqy2ma6ecGURWSMpmNeVCHiD2' or uid == 'yleZdWDZgFYTBxwzC5NtHVeb3733':
    #     praproval = True 
    # if  uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
    #     aiaccess = True    

    context = {
        # "tl": istl,
        "name":name,
        "dep":dep,
        # "accounts": accounts,
        # "management": management,
        # "itaproval":itaproval,
        # "rndaproval":rndaproval,
        # "praproval":praproval,
        # "aiaccess":aiaccess
    }
    if request.method == "POST":
        msg = request.POST['msg']
        tm = datetime.now()
        date_time = tm.strftime("%Y-%m-%d_%H:%M:%S")
        date = tm.strftime("%Y-%m-%d")
        time = tm.strftime("%I:%M:%S %p")
        val = {
            "message":msg,
            "date": date,
            "time":time,
            "isread":False
        }
        db.child('suggestion').child(current_year).child(current_month).child(formatted_date).push(val)
        context = {
            "msg":"Message sent successfully",
            # "accounts": accounts,
            # "management":management,
            # "tl": istl,
            # "dep":dep,
            # "rndaproval":rndaproval,
            # "itaproval":itaproval,
            # "praproval":praproval,
            # "aiaccess":aiaccess
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
    # name=db.child("staff").child(uid).child("name").get().val()
    name = checkUserName(uid)
    istl = False
    praproval = False
    tl = db.child("tl").get().val()
    for t in tl:
        if name == tl[t]:
            istl = True
            break
    if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
        praproval = True    
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1    
    accounts = False
    if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
        accounts = True
        
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
            "tl": istl,
            "accounts": accounts,
            "suggestionNotification":suggestionNotification,
            "container": True,
            "praproval":praproval
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
        "tl": istl,
        "accounts": accounts,
        "suggestionNotification":suggestionNotification,
        "container": True,
        "praproval":praproval
    }
    return render(request, "financial.html", context)

def inventorymanagement(request):
    return render(request,'inventorymanagement.html')
def coohome(request):
    return render(request,'coohome.html')
def installation_details(request):
    return render(request,'installation_details.html')
def todo(request):
    return render(request,'todo.html')
def refreshment(request):
    if request.method == "POST":
        todayDate = str(date.today())
        currTime = datetime.now().strftime("%H:%M")
        selected_refreshments = request.POST.getlist("refreshment")
        d = db.child("refreshments").get().val()
        uid = request.COOKIES["uid"]
        _name = checkUserName(uid)
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
                        db.child("refreshments").child(todayDate).child("Lunch").child("lunch_list").update({"name" + str(a + 1): _name})
                        d = db.child("refreshments").get().val()
                        newLen = len(d[todayDate][choosen]["lunch_list"])
                        db.child("refreshments").child(todayDate).child("Lunch").update({choosen + "_count": newLen})
    
        return redirect('ithome')
    
def submitwork(request):
    uid = request.COOKIES["uid"]
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
            return redirect('ithome')
    return render(request, "ithome.html")   

def editworkdone(request):
    uid = request.COOKIES["uid"]
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
    return redirect('ithome')

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
    return render(request,'admindashboard.html')

def userdata(request):
    uid = request.COOKIES["uid"]
    # aiaccess = False
    # adminai = False
    # aiteam = False

    # userdata = aidb.child("onyx").get().val()
    # if uid == "Vhbt8jIAfiaV1HxuWERLqJh7dbj2" or uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
    #     aiaccess = True
    # if uid == "Vhbt8jIAfiaV1HxuWERLqJh7dbj2":
    #     adminai=True
    # if uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
    #     aiteam =True

    userdata = aidb.child("onyx").get().val()
    no_data_message = ""  
    default_data = {}  
    like_data = {} 
    dislike_data = {} 

    print("==")
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
        # "aiaccess": aiaccess,
        "default_data": default_data,
        "like_data": like_data,
        "dislike_data": dislike_data,
        "no_data_message": no_data_message,
        # "aiteam": aiteam,
        # "adminai": adminai
    } 
    return render(request,'userdata.html',context)    