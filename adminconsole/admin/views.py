from django.shortcuts import render
import pyrebase
from datetime import datetime
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
    return render(request,'adminhome.html')
def checkin(request):
    return render(request,'checkin.html')

def attendanced(request):
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
    staff=db.child("staff").get().val()
    leaveapplied=db.child("leaveDetails").child(current_year).child(current_month).get().val()
    attendance=db.child("attendance").child(current_year).child(current_month).get().val()
    leavecountlist=[]
    staffpresentlist=[]
    staffnamelist=[]
    staffuidlist=[]
    snolist=[]
    staffdeplist=[]
    sno=0
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

        attendancelistall=zip(snolist,staffuidlist,staffnamelist,staffdeplist,staffpresentlist,leavecountlist)
        context={
            "attendancelistall":attendancelistall
        }
    return render(request,'attendanced.html',context)

def indvattendanced(request):
    return render(request,'indvattendanced.html')