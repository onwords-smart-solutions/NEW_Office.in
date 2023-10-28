from django.shortcuts import render
from adminconsole.views import db, checkUserName,checkUserDepartment
from datetime import datetime, timedelta
import pyrebase
from datetime import datetime,timedelta
from it.views import convert_to_12_hour_format,calculate_progress,calculate_progress_
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
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
    current_date1 = datetime.now().strftime("%d")
    current_date_today = datetime.now().strftime("%Y-%m-%d")
    current_date = datetime.now()

    staff=db.child("staff").get().val()
    attendance=db.child("attendance").child(current_year).child(current_month).get().val()
    attendance1=db.child("attendance").child(current_year).get().val()
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
        month = days[5:7]
        days = days[8:10]
        totalstafftotalabsent=0
        totalstafftotalpresent=0
        for staffuid in staff:
            if staff[staffuid]["department"] != "ADMIN":
                try:
                    attendance1[month][days]
                    try:
                        attendance1[month][days][staffuid]
                        totalstafftotalpresent=totalstafftotalpresent+1
                    except:
                        totalstafftotalabsent=totalstafftotalabsent+1
                except:
                    pass        

        allpresentlist.append(totalstafftotalpresent)
        allabsentlist.append(totalstafftotalabsent)   
    weeklypresentlist=zip(allpresentlist,allabsentlist,alldatelist)
    data = db.child("staff").get().val()
    attendence = db.child("attendance").get().val()
    workmanager = db.child("workmanager").get().val()
    leavedetails = db.child("leave_details").get().val()
    name = checkUserName(uid)
    istl = False
    itaproval = False
    aiaccess = False
    tl = db.child("tl").get().val()

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
    for t in tl:
        if name == tl[t]:
            istl = True
            break
    if  uid == 'jDYzpwcpv3akKaoDL9N4mllsGCs2':
        itaproval = True  
    if  uid == "cQ4gFReQghZruTCDMP9NZgwMCzM2" or uid == "NH8ePNnoCtbmTvBbFdV2koxBIhR2":
        aiaccess = True   
    try:
        try:
            todaycheckin = attendence[current_year][current_month][current_day][uid]["check_in"]
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
        except:
            yesterdayprogress = "Absent"    
        try:
            today_progress= calculate_progress_(todaycheckin, todaycheckout)
        except:
            today_progress= "Absent"
        todaycheckout = convert_to_12_hour_format(todaycheckout)
        todaycheckin = convert_to_12_hour_format(todaycheckin)   

        listOfTodaysWork= []
        try:
            for z in workmanager[current_year][current_month][formatted_date][uid]:
                listOfTodaysWork.append(workmanager[current_year][current_month][formatted_date][uid][z])
        except:        
            listOfTodaysWork.append("No Workdone") 
        try:    
            for work_item in listOfTodaysWork:
                if 'workPercentage' in work_item:
                    work_item['workPercentage'] = work_item['workPercentage'].replace('%', '').strip()
        except:
            pass

        try:
            generalcount = 0
            sickcount = 0
            leavedata = db.child("leave_details").get().val()
            yearList, monthList, dateList, typelist, datalist = [], [], [], [], []
            for allMonths in leavedata[current_year]:

                months = leavedata[current_year][allMonths]
                for allDates in months:
                    try:
                        le = leavedata[current_year][allMonths][allDates][uid]
                        for leave_type, leave_info in le.items():
                            if leave_type == "general":
                                generalcount+=1
                            if leave_type == "sick":
                                sickcount+=1    
                            types = leave_type
                            data = leave_info
                            yearList.append(current_year)
                            monthList.append(allMonths)
                            dateList.append(allDates)
                            typelist.append(types)
                            datalist.append(data)
                    except:
                        pass
            
            leavehistory = zip(yearList, monthList, dateList, typelist, datalist)
            context = {
                "leavehistory": leavehistory,
                "dep":dep,
                "name":name,
                "profile":profile,
                # "tl": istl,
                # "dep":dep,
                # "accounts":accounts,
                # "management":management,
                "suggestionNotification":suggestionNotification
            }
        except:
            pass 
                    
        generalleave = 24 - generalcount
        sickleave = 12 - sickcount  
        overallleave = generalleave + sickleave 
        data[uid]["projects"]
        context={
            "project": True,
            "name":name,
            "dep":dep,
            "profile":profile,
            "allpresentlist":allpresentlist,
            "allabsentlist":allabsentlist,
            "current_date_today":current_date_today,
            "stafftotalpresent":stafftotalpresent,
            "stafftotalabsent":stafftotalabsent,
            "weeklypresentlist":weeklypresentlist,
            "itaproval": itaproval,
            "aiaccess": aiaccess,
            "todaycheckin": todaycheckin,
            "todaycheckout": todaycheckout,
            "yescheckin": yesscheckin,
            "yescheckout": yesscheckout,
            "yesprogress":yesterdayprogress,
            "todayprogress":today_progress,
            "listOfTodaysWork" : listOfTodaysWork,
            "day":day,
            "generalleave":generalleave,
            "sickleave":sickleave,
            "overallleave":overallleave,
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
        return render(request,'adminhome.html',context)
    except:
        context={
                "project": False,
                "name": name,
                "tl": istl,
                "dep": dep,
                "profile":profile,
                "allpresentlist":allpresentlist,
                "allabsentlist":allabsentlist,
                "current_date_today":current_date_today,
                "stafftotalpresent":stafftotalpresent,
                "stafftotalabsent":stafftotalabsent,
                "weeklypresentlist":weeklypresentlist,
                "itaproval": itaproval,
                "aiaccess": aiaccess,
                "todaycheckin": todaycheckin,
                "todaycheckout": todaycheckout,
                "yescheckin": yesscheckin,
                "yescheckout": yesscheckout,
                "yesprogress":yesterdayprogress,
                "todayprogress":today_progress,
                "listOfTodaysWork":listOfTodaysWork,
                "day":day,
                "generalleave":generalleave,
                "sickleave":sickleave,
                "overallleave":overallleave,
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
        return render(request,'adminhome.html',context)

def checkin(request):
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
        if form_type == 'presentForm':
            dates = request.POST.get("date")
            current_date = datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d")
            dates1 = formatted_date
        elif form_type == 'absentForm':
            dates1 = request.POST.get("date")
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
    date_parts = dates1.split("-")
    tyear = date_parts[0]
    tmonth = date_parts[1]
    tday = date_parts[2]   

    leavedetails=db.child("leave_details").get().val()
    alltypes=[]
    allstatus=[]
    allnames=[]
    for uid in staffDB:
        try:
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
        "profile":profile,
        "request": request,
        "finallist": sorted_finallist,
        "absenteeslist":absentworkinghourlist,
        "totalcount":total_staff_count,
        "presentcount":present_staff_count,
        "absentcount":absent_staff_count,
        "date":dates,
        "allabsentees":absenteeslistwithstatus,
        "date1":dates1,
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
    return render(request,'checkin.html',context) 

def attendanced(request):
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
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%m")
    current_date = datetime.now().strftime("%Y-%m-%d")
    staff=db.child("staff").get().val()
    leaveapplied=db.child("leave_details").child(current_year).child(current_month).get().val()
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
            try:
                for date in leaveapplied:
                    try:
                        for leavetype in leaveapplied[date][staffuid]:
                            if leavetype != "permission":
                                staffleavecount=staffleavecount+1 
                    except:
                        pass
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
            "profile":profile,
            "attendancelistall":attendancelistall,
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
    return render(request,'attendanced.html',context)

def attendancesort(request):
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
    if request.method =="POST":
        date1=request.POST["get-total1"]
        uid = request.COOKIES["uid"]
        dep = request.COOKIES["dep"]
        profile=request.COOKIES["profile"]
        name = request.COOKIES["name"]
        todaysDate=str(date1)
        current_year = todaysDate[:4]
        current_month = todaysDate[5:7]
        staff=db.child("staff").get().val()
        leaveapplied=db.child("leave_details").child(current_year).child(current_month).get().val()
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
        return render(request,'attendanced.html',context)

def indvattendanced(request):
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
    getuid=request.POST["suid"]
    date=request.POST["date"]
    name=checkUserName(getuid)
    dep=checkUserDepartment(getuid)
    current_year = date[:4]
    current_month = date[4:6]
    staff=db.child("staff").get().val()
    datelist,leavetypelist,leavenode,permissioncountlist = [],[],[],[]
    leaveapplied=db.child("leave_details").child(current_year).child(current_month).get().val()
    generalleavecount=0
    sickleavecount=0
    try:
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
    except:
        pass                            
    permissioncount = 0.0
    for time_str in permissioncountlist:
        hours, minutes = map(int, time_str.split(':'))
        permissioncount += hours + minutes / 60.0                        
    leaveall=zip(datelist,leavetypelist,leavenode)                        
    context={
        "name":name,
        "dep":dep,
        "profile":profile,
        "leaveall":leaveall,
        "permissioncount":permissioncount,
        "sickleavecount":sickleavecount,
        "generalleavecount":generalleavecount,
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
    return render(request,'indvattendanced.html',context)