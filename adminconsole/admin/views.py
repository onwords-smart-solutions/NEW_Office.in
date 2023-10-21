from django.shortcuts import render
import pyrebase
from datetime import datetime,timedelta
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
db = firebase.database()
auth = firebase.auth()
storage1 = firebase.storage()

firebase1 = pyrebase.initialize_app(firebaseConfig)
db1 = firebase1.database()
storage = firebase1.storage()
# Create your views here.
def adminhome(request):
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
    print(stafftotalpresent,stafftotalabsent)            
    start_of_week = current_date - timedelta(days=current_date.weekday() + 1)
    days_of_week = [start_of_week + timedelta(days=i) for i in range(1,7)]
    weekdaylist=[]
    for day in days_of_week:
        # print(day.strftime("%Y-%m-%d"))
        weekdaylist.append(day.strftime("%Y-%m-%d"))
    allpresentlist,allabsentlist,alldatelist=[],[],[]

    for days in weekdaylist:
        print(days)
        totalstafftotalabsent=0
        totalstafftotalpresent=0
        for staffuid in staff:
            if staff[staffuid]["department"] != "ADMIN":
                try:
                    attendance[str(days)][staffuid]
                    totalstafftotalpresent=totalstafftotalpresent+1
                except:
                    totalstafftotalabsent=totalstafftotalabsent+1

        allpresentlist.append(totalstafftotalpresent)
        allabsentlist.append(totalstafftotalabsent)
    # print(allpresentlist,allabsentlist)   
    weeklypresentlist=zip(allpresentlist,allabsentlist,alldatelist)    
    context={
        "allpresentlist":allpresentlist,
        "allabsentlist":allabsentlist,
        "current_date_today":current_date_today,
        "stafftotalpresent":stafftotalpresent,
        "stafftotalabsent":stafftotalabsent,
        "weeklypresentlist":weeklypresentlist
    }     
    return render(request,'adminhome.html',context)

def checkin(request):
    return render(request,'checkin.html')

def attendanced(request):
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
    current_date = datetime.now().strftime("%Y-%m-%d")
    staff=db.child("staff").get().val()
    leaveapplied=db.child("leaveDetails").child(current_year).child(current_month).get().val()
    attendance=db.child("attendance").child(current_year).child(current_month).get().val()
    leavecountlist=[]
    staffpresentlist=[]
    staffnamelist=[]
    staffuidlist=[]
    snolist=[]
    staffdeplist=[]
    datelist=[]
    sno=0
    stafftotalpresent=0
    stafftotalabsent=0
    for staffuid in staff:
        try:
            attendance[current_date][staffuid]
            stafftotalpresent=stafftotalpresent+1
        except:
            stafftotalabsent=stafftotalabsent+1

    for staffuid in staff:
        if staff[staffuid]["department"]!="ADMIN":
            staffleavecount=0
            for date in leaveapplied:
                try:
                    for leavetype in leaveapplied[date][staffuid]:
                        staffleavecount=staffleavecount+1 
                except:
                    pass
            staffattendancecount=0
            for date in attendance:
                try:
                    attendance[date][staffuid]
                    staffattendancecount=staffattendancecount+1
                except:
                    pass
            sno=sno+1    
            snolist.append(sno)  
            staffuidlist.append(staffuid)   
            staffnamelist.append(staff[staffuid]["name"])
            staffdeplist.append(staff[staffuid]["department"])
            staffpresentlist.append(staffattendancecount)
            leavecountlist.append(staffleavecount)
            datelist.append(current_year+current_month)
        attendancelistall=zip(snolist,staffuidlist,staffnamelist,staffdeplist,staffpresentlist,leavecountlist,datelist)
        context={
            "attendancelistall":attendancelistall
        }
    return render(request,'attendanced.html',context)

def attendancesort(request):
    if request.method =="POST":
        date1=request.POST["get-total1"]
        print(date1)
        uid = request.COOKIES["uid"]
        dep = request.COOKIES["dep"]
        name = checkUserName(uid)
        todaysDate=str(date1)
        current_year = todaysDate[:4]
        current_month = todaysDate[5:7]
        staff=db.child("staff").get().val()
        leaveapplied=db.child("leaveDetails").child(current_year).child(current_month).get().val()
        attendance=db.child("attendance").child(current_year).child(current_month).get().val()
        leavecountlist=[]
        staffpresentlist=[]
        staffnamelist=[]
        staffuidlist=[]
        snolist=[]
        staffdeplist=[]
        datelist=[]
        sno=0
        for staffuid in staff:
            if staff[staffuid]["department"]!="ADMIN":
                staffleavecount=0
                try:
                    for date in leaveapplied:
                        try:
                            for leavetype in leaveapplied[date][staffuid]:
                                staffleavecount=staffleavecount+1 
                        except:
                            pass
                except:
                    pass
                staffattendancecount=0
                try:    
                    for date in attendance:
                        try:
                            attendance[date][staffuid]
                            staffattendancecount=staffattendancecount+1
                        except:
                            pass
                except:
                    pass        
                sno=sno+1    
                snolist.append(sno)  
                staffuidlist.append(staffuid)   
                staffnamelist.append(staff[staffuid]["name"])
                staffdeplist.append(staff[staffuid]["department"])
                staffpresentlist.append(staffattendancecount)
                leavecountlist.append(staffleavecount)
                datelist.append(current_year+current_month)

        attendancelistall=zip(snolist,staffuidlist,staffnamelist,staffdeplist,staffpresentlist,leavecountlist,datelist)
        context={
            "attendancelistall":attendancelistall
        }
        return render(request,'attendanced.html',context)

def checkUserName(uid):
    data = db.child("staff").get().val()
    for x in data:
        if uid == x:
            z = data[x]["name"]
            return z
def indvattendanced(request):
    getuid=request.POST["suid"]
    date=request.POST["date"]
    print(date)
    current_year = date[:4]
    current_month = date[4:6]
    staff=db.child("staff").get().val()
    leaveapplied=db.child("leaveDetails").child(current_year).child(current_month).get().val()
    return render(request,'indvattendanced.html')
