from django.shortcuts import render
from adminconsole.views import db, checkUserName,checkUserDepartment
from datetime import datetime, timedelta
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
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
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
          
    start_of_week = current_date - timedelta(days=current_date.weekday() + 1)
    days_of_week = [start_of_week + timedelta(days=i) for i in range(1,7)]
    weekdaylist=[]
    for day in days_of_week:
        weekdaylist.append(day.strftime("%Y-%m-%d"))
    allpresentlist,allabsentlist,alldatelist=[],[],[]
    for days in weekdaylist:
        current_year = days[:4]
        days = days[8:10]
        totalstafftotalabsent=0
        totalstafftotalpresent=0
        for staffuid in staff:
            if staff[staffuid]["department"] != "ADMIN":
                try:
                    attendance[days][staffuid]
                    totalstafftotalpresent=totalstafftotalpresent+1
                    print(totalstafftotalpresent)
                except:
                    totalstafftotalabsent=totalstafftotalabsent+1

        allpresentlist.append(totalstafftotalpresent)
        allabsentlist.append(totalstafftotalabsent)
    weeklypresentlist=zip(allpresentlist,allabsentlist,alldatelist)    
    context={
        "name":name,
        "dep":dep,
        "allpresentlist":allpresentlist,
        "allabsentlist":allabsentlist,
        "current_date_today":current_date_today,
        "stafftotalpresent":stafftotalpresent,
        "stafftotalabsent":stafftotalabsent,
        "weeklypresentlist":weeklypresentlist
    }     
    return render(request,'adminhome.html',context)

def checkin(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    attendance = db.child("attendance").get().val()
    staffDB = db.child("staff").get().val()
    todaysDate = datetime.today()
    thisDa = todaysDate.strftime("%d")
    currentyear = todaysDate.strftime("%Y")
    currentmonth = todaysDate.strftime("%m")
    staffuid=[]
    staffnamelist=[]
    attendenceloginlist=[]
    attendencelogoutlist=[]
    workinghourlist=[]
 
    attype=[]
    outtype=[]
    absentstaff =[]
    absentworkinghours=[]
    workinghourlistall=[]
    
    # todaysDate = datetime.today()
    # yesterdayDate = todaysDate - timedelta(days=1)
    # formattedYesterdayDate = yesterdayDate.strftime("%Y-%m-%d")
    # dates = [formattedYesterdayDate]
    # dates=["2023-10-16"]
    # for date1 in dates:
    #     # dailyworkhours(date1)
    #     date_parts = date1.split("-")
    #     tyear = date_parts[0]
    #     tmonth = date_parts[1]
    #     tday = date_parts[2] 
    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        print("form",form_type)    
        if form_type == 'presentForm':
            dates = request.POST.get("date")
            current_date = datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d")
            dates1 = formatted_date
        elif form_type == 'absentForm':
            dates1 = request.POST.get("date")
            print("dates1",dates1)
            todaysDate = datetime.today()
            yesterdayDate = todaysDate - timedelta(days=1)
            if yesterdayDate.weekday() == 6:  
                saturdayDate = yesterdayDate - timedelta(days=1)
                dates = saturdayDate.strftime("%Y-%m-%d")
            else:
                dates = yesterdayDate.strftime("%Y-%m-%d")
        else:
            pass
            
    else:
        todaysDate = datetime.today()
        yesterdayDate = todaysDate - timedelta(days=1)
        if yesterdayDate.weekday() == 6: 
            saturdayDate = yesterdayDate - timedelta(days=1)
            dates = saturdayDate.strftime("%Y-%m-%d")
        else:
            dates = yesterdayDate.strftime("%Y-%m-%d")

        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")
        dates1 = formatted_date
    
  
    date_parts = dates.split("-")
    tyear = date_parts[0]
    tmonth = date_parts[1]
    tday = date_parts[2]   
    try:
        attend = attendance[tyear][tmonth][tday]
    except:
        pass    
    
    for staff in staffDB:
        try:
            if staffDB[staff]['department'] != "ADMIN":
                try:
                    checkin = attend[staff].get("check_in", None)
                    checkout = attend[staff].get("check_out", None)
                    workinghour = attend[staff]["working_hours"]

                    try:
                        if checkin is not None and checkout is not None and workinghour is not None:     
                            date_format = "%Y-%m-%d %H:%M:%S"
                            common_date = datetime.now().date()
                            datetime1 = datetime.strptime(str(common_date) + " " + checkin, date_format)
                            datetime2 = datetime.strptime(str(common_date) + " " + checkout, date_format)
                            datetimeall1 = datetime.strptime(str(datetime1), date_format)
                            datetimeall2 = datetime.strptime(str(datetime2), date_format)
                            time_string1 = datetimeall1.strftime("%I:%M:%S %p")
                            time_string2 = datetimeall2.strftime("%I:%M:%S %p")

                            staffnamelist.append(staffDB[staff]["name"])
                            attendenceloginlist.append(time_string1)
                            attendencelogoutlist.append(time_string2)
                            workinghourlist.append(workinghour)
                            staffuid.append(staff)
                        
    
                            try:
                                checkintype = attend[staff]["proxy_in"]
                                attype.append("proxy")
                            except:
                                attype.append("Id Card")   
                            try:     
                                checkouttype = attend[staff]["proxy_out"]
                                outtype.append("proxy")
                            except:
                                outtype.append("Id Card")

                        elif checkin is not None and workinghour is not None:
                            date_format = "%Y-%m-%d %H:%M:%S"
                            common_date = datetime.now().date()
                            datetime1 = datetime.strptime(str(common_date) + " " + checkin, date_format)
                            datetimeall1 = datetime.strptime(str(datetime1), date_format)
                            time_string1 = datetimeall1.strftime("%I:%M:%S %p")

                            staffnamelist.append(staffDB[staff]["name"])
                            attendenceloginlist.append(time_string1)
                            attendencelogoutlist.append("No entry")
                            workinghourlist.append(workinghour)
                            staffuid.append(staff)
            
                            try:
                                checkintype = attend[staff]["proxy_in"]
                                attype.append("proxy")
                            except:
                                attype.append("Id Card")   
                            try:     
                                checkouttype = attend[staff]["proxy_out"]
                                outtype.append("proxy")
                            except:
                                outtype.append("No entry")
                        


                        try:
                            total = attendance[currentyear][currentmonth]
                            totalhours = 0   
                            for date in total:
                                dailyhours = total.get(date,{}).get(staff, {}).get("working_hours",0)       
                                try:   
                                    hours, minutes, seconds = map(int, dailyhours.split(':')) 
                                    workinghourall = hours * 3600 + minutes * 60 + seconds
                                except:
                                    workinghourall = 0    
                                totalhours+=workinghourall 

                            total_hours, remainder = divmod(totalhours, 3600)
                            total_minutes, total_seconds = divmod(remainder, 60)
                            workinghourlistall.append(f"{total_hours:02}:{total_minutes:02}:{total_seconds:02}")
                        except:
                            workinghourlistall.append("No Logs")        
                    except:
                        pass        
                
                except:
                    absentstaff.append(staffDB[staff]["name"])
                    try:
                        total = attendance[currentyear][currentmonth]
                        totalhours = 0   
                        for date in total:
                            dailyhours = total.get(date,{}).get(staff, {}).get("working_hours",0)
                            try:   
                                hours, minutes, seconds = map(int, dailyhours.split(':')) 
                                workinghourall = hours * 3600 + minutes * 60 + seconds
                            except:
                                workinghourall = 0    
                            totalhours+=workinghourall 
                        total_hours, remainder = divmod(totalhours, 3600)
                        total_minutes, total_seconds = divmod(remainder, 60)
                        # staffnamelist.append(data[staffuid]["name"])
                        absentworkinghours.append(f"{total_hours:02}:{total_minutes:02}:{total_seconds:02}")
                    except:
                        absentworkinghours.append("No Logs")
        except:
            pass                
    
    total_staff_count = len(staffDB)
    present_staff_count = total_staff_count - len(absentstaff)
    absent_staff_count = len(absentstaff)

    try:
        sorted_finallist = sorted(zip(staffnamelist,attendenceloginlist,attendencelogoutlist,workinghourlist,workinghourlistall,attype,outtype), key=lambda x: x[0])
        absentworkinghourlist = sorted(zip(absentstaff, absentworkinghours), key=lambda x: x[0])
    except:
        sorted_finallist = []
    print("dates1",dates1)
    date_parts = dates1.split("-")
    tyear = date_parts[0]
    tmonth = date_parts[1]
    tday = date_parts[2]   

    leavedetails=db.child("leaveDetails").get().val()
    alltypes=[]
    allstatus=[]
    allnames=[]
    for uid in staffDB:
        try:
            print("uid",uid)
            types=leavedetails[tyear][tmonth][dates1][uid]
            for leave_type, details in types.items():
                alltypes.append(leave_type)
                allstatus.append(details["status"])
                allnames.append(details["name"])
        except:
            pass 
    absenteeslistwithstatus=zip(allnames,alltypes,allstatus)           

    context = {
        "name":name,
        "dep":dep,
        "request": request,
        "finallist": sorted_finallist,
        "absenteeslist":absentworkinghourlist,
        "totalcount":total_staff_count,
        "presentcount":present_staff_count,
        "absentcount":absent_staff_count,
        "date":dates,
        "allabsentees":absenteeslistwithstatus,
        "date1":dates1
    }
    return render(request,'checkin.html',context) 


def attendanced(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
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
                        if leavetype != "permission":
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
            "name":name,
            "dep":dep,
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
            "attendancelistall":attendancelistall,
            "dep":dep,
            "name":name
        }
        return render(request,'attendanced.html',context)

def indvattendanced(request):
    getuid=request.POST["suid"]
    date=request.POST["date"]
    print(date,getuid)
    name=checkUserName(getuid)
    dep=checkUserDepartment(getuid)
    current_year = date[:4]
    current_month = date[4:6]
    staff=db.child("staff").get().val()
    datelist,leavetypelist,leavenode,permissioncountlist = [],[],[],[]
    leaveapplied=db.child("leaveDetails").child(current_year).child(current_month).get().val()
    generalleavecount=0
    sickleavecount=0
    for date in leaveapplied:
        for uid in leaveapplied[date]:
            if uid == getuid:
                for leavetype in leaveapplied[date][uid]:
                    datelist.append(date)
                    if leavetype == "permission":
                        leavetypelist.append(leavetype)
                        leavenode.append(leaveapplied[date][uid][leavetype]["duration"])
                        permissioncountlist.append(leaveapplied[date][uid][leavetype]["duration"])
                    elif leavetype == "sick":
                        leavetypelist.append(leavetype)
                        if leaveapplied[date][uid][leavetype]["node"] == "Full Day":
                            leavenode.append("Full Day")
                            sickleavecount=sickleavecount+1
                        else:
                            leavenode.append("Half Day")
                            sickleavecount=sickleavecount+0.5    
                    else:
                        leavetypelist.append(leavetype)
                        if leaveapplied[date][uid][leavetype]["node"] == "Full Day":
                            leavenode.append("Full Day")
                            generalleavecount=generalleavecount+1 
                        else:
                            leavenode.append("Half Day")
                            generalleavecount=generalleavecount+0.5
    permissioncount = 0.0
    for time_str in permissioncountlist:
        hours, minutes = map(int, time_str.split(':'))
        permissioncount += hours + minutes / 60.0                        
    print(datelist,leavetypelist,leavenode)
    leaveall=zip(datelist,leavetypelist,leavenode)                        
    context={
        "name":name,
        "dep":dep,
        "leaveall":leaveall,
        "permissioncount":permissioncount,
        "sickleavecount":sickleavecount,
        "generalleavecount":generalleavecount
    }
    return render(request,'indvattendanced.html',context)