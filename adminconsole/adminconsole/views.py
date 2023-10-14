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

firebase = pyrebase.initialize_app(config)
db1 = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

firebase1 = pyrebase.initialize_app(firebaseConfig)
db = firebase1.database()

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
            # if dep == "MEDIA":
            #     response = redirect("mediahome")
            #     return response
            # if dep == "PR":
            #     response = redirect("prhome")
            #     return response
            # if dep == "RND":
            #     response = redirect("rndhome")
            #     return response
            # if dep == "ADMIN":
            #     response = redirect("adminhome")
            #     return response
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
                response = redirect("mediahome")
                response.set_cookie("uid", uid, expires=exp)
                response.set_cookie("dep", dep, expires=exp)
                response.set_cookie("loginState", "loggedIn", expires=exp)
                return response
            if dep == "PR":
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
    return render(request,'leave-form.html')
def late_form(request):
    return render(request,'late_form.html')
def leave_approval(request):
    return render(request,'approval.html')
def suggestion(request):
    return render(request,'suggestion.html')
def financial(request):
    return render(request,'financial.html')
<<<<<<< HEAD
def cmoproduct(request):
    return render(request,'cmoproduct.html')
=======
def coohome(request):
    return render(request,'coohome.html')
def installation_details(request):
    return render(request,'installation_details.html')
>>>>>>> 94157cc5f84f6180f0dc5ee00d429151339c319f



def refreshment(request):
    if request.method == "POST":
        todayDate = str(date.today())
        currTime = datetime.now().strftime("%H:%M")
        print("time",currTime)
        selected_refreshments = request.POST.getlist("refreshment")
        print("ref",selected_refreshments)
        d = db.child("refreshments").get().val()
        uid = request.COOKIES["uid"]
        _name = checkUserName(uid)
        for choosen in selected_refreshments:
            print("for",choosen)
            if choosen == "tea":
                print("choose",choosen)
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
            
            print("choosen",choosen)
            if choosen == "Lunch":
                if currTime < "14:00":
                    print("entering")
                    try:
                        print("==")
                        d[todayDate][choosen]["lunch_list"]
                        print("start")
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
        print("===")
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

def lateentry(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    loginState = request.COOKIES["loginState"]
    form_submitted = False
    name = checkUserName(uid)
    istl = False
    accounts = False
    itaproval = False
    rndaproval = False
    praproval = False
    aiaccess = False
    tl = db.child("tl").get().val()
    for t in tl:
        if name == tl[t]:
            istl = True
            break
    if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" or uid == 'Vhbt8jIAfiaV1HxuWERLqJh7dbj2':
        accounts = True

    if  uid == 'jDYzpwcpv3akKaoDL9N4mllsGCs2':
        itaproval = True

    if  uid == 'pztngdZPCPQrEvmI37b3gf3w33d2':
        rndaproval = True
    if  uid == 'tQYuqy2ma6ecGURWSMpmNeVCHiD2' or uid == 'yleZdWDZgFYTBxwzC5NtHVeb3733':
        praproval = True 
    if  uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
        aiaccess = True            

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
                "aiaccess":aiaccess
            }
            childName = ft + " to " + tt
            db.child("staff").child(uid).child("workManager").child("timeSheet").child(selectedYear).child(selectedMonth).child(sd).child(
                "LateEntry"
            ).child(childName).set(context)
            
    return render(request, "lateentry.html", {"form_submitted": form_submitted, "dep":dep, "tl": istl, "accounts":accounts,  "itaproval":itaproval, "rndaproval":rndaproval,"praproval":praproval,"aiaccess":aiaccess})


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

def logout(request):
    response = redirect("login")
    response.delete_cookie("uid")
    response.delete_cookie("loginState")
    return response            
