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
  "apiKey": "AIzaSyAVVGMgQ4hzstzNBx4k6SThBW1HuCY4yKg",
  "authDomain": "newadminconsole.firebaseapp.com",
  "databaseURL": "https://newadminconsole-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "newadminconsole",
  "storageBucket": "newadminconsole.appspot.com",
  "messagingSenderId": "374033060149",
  "appId": "1:374033060149:web:1d6ad9d0779562dc513c7c",
  "measurementId": "G-GYNJ4LQP93"
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
    
        return render(request, "ithome.html")

def checkUserDepartment(uid):
    data = db.child("staff").get().val()
    for x in data:
        if uid == x:
            dep = data[x]["department"]
            return dep

def checkUserName(uid):
    data = db.child("staff").get().val()
    for x in data:
        if uid == x:
            z = data[x]["name"]
            return z