from django.shortcuts import render
from django.shortcuts import render
from adminconsole.views import db, checkUserName
from it.views import convert_to_12_hour_format,calculate_progress,calculate_progress_
from datetime import datetime,timedelta
# Create your views here.

def hrhome(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
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
    current_date1 = datetime.now().strftime("%d")
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
        day1 = False
        try:
            if yesterday.weekday() == 6:
                yescheckin = attendence[saturday_year][saturday_month][saturday_day][uid]["check_in"]
                day1 = "Saturday"
                yesscheckin = convert_to_12_hour_format(yescheckin)
            else:
                # If yesterday was not a Sunday, use the existing code for Sunday data
                yescheckin = attendence[yesterday_year][yesterday_month][yesterday_day][uid]["check_in"]
                yesscheckin = convert_to_12_hour_format(yescheckin)
                day1 = False
        except:
            yesscheckin = "No Entry"
        

        try:
            if yesterday.weekday() == 6:
                # If yesterday was a Sunday, retrieve Saturday data
                
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
                # "tl": istl,
                # "dep":dep,
                # "accounts":accounts,
                # "management":management,
                "suggestionNotification":suggestionNotification
            }
        except:
            pass 
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
    
        generalleave = 24 - generalcount
        sickleave = 12 - sickcount  
        overallleave = generalleave + sickleave 
        data[uid]["projects"]
        context = {
            "project": True,
            "name": name,
            "tl": istl,
            "dep": dep,
            "profile":profile,
            "itaproval": itaproval,
            "aiaccess": aiaccess,
            "todaycheckin": todaycheckin,
            "todaycheckout": todaycheckout,
            "yescheckin": yesscheckin,
            "yescheckout": yesscheckout,
            "yesprogress":yesterdayprogress,
            "todayprogress":today_progress,
            "listOfTodaysWork" : listOfTodaysWork,
            "day":day1,
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
            "suggestionNotification":suggestionNotification,
            "allpresentlist":allpresentlist,
            "allabsentlist":allabsentlist,
            "weeklypresentlist":weeklypresentlist,
            "stafftotalpresent":stafftotalpresent,
            "stafftotalabsent":stafftotalabsent
        }
        return render(request, "hrhome.html", context)
    except:
        context = {
            "project": False,
            "name": name,
            "tl": istl,
            "dep": dep,
            "profile":profile,
            "itaproval": itaproval,
            "aiaccess": aiaccess,
            "todaycheckin": todaycheckin,
            "todaycheckout": todaycheckout,
            "yescheckin": yesscheckin,
            "yescheckout": yesscheckout,
            "yesprogress":yesterdayprogress,
            "todayprogress":today_progress,
            "listOfTodaysWork":listOfTodaysWork,
            "day":day1,
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
            "suggestionNotification":suggestionNotification,
            "allpresentlist":allpresentlist,
            "allabsentlist":allabsentlist,
            "weeklypresentlist":weeklypresentlist,
            "stafftotalpresent":stafftotalpresent,
            "stafftotalabsent":stafftotalabsent,
        }
    return render(request,'hrhome.html',context)
