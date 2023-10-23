from django.shortcuts import render
from django.shortcuts import redirect
from adminconsole.views import db, checkUserName

# Create your views here.
def superadmin(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    context = {
        "name":name,
        "dep":dep,
    }
    return render(request,'superadmin.html',context)
def createstaff(request):
    return render(request,'createstaff.html')
def staffaccess(request):
    return render(request,'staff-access.html')

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