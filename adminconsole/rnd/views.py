from django.shortcuts import render,redirect
from adminconsole.views import db, checkUserName
from it.views import convert_to_12_hour_format,calculate_progress,calculate_progress_
from datetime import datetime,timedelta
from django.contrib import messages
import pyrebase
# Create your views here.

config2 = {
    "apiKey": "AIzaSyAZcnME1iLaqUWHtnWfnwvyp3_7h1Qdng",
    "authDomain": "smart-home-c08c4.firebaseapp.com",
    "databaseURL": "https://smart-home-c08c4-default-rtdb.firebaseio.com",
    "projectId": "smart-home-c08c4",
    "storageBucket": "smart-home-c08c4.appspot.com",
    "messagingSenderId": "867325064971",
    "appId": "1:867325064971:web:03089586292c3ed943540e",
    "measurementId": "G-01LGYRSE6M",
}
firebase2 = pyrebase.initialize_app(config2)
shDB = firebase2.database()

def rndhome(request):
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
                    
        generalleave = 24 - generalcount
        sickleave = 12 - sickcount  
        overallleave = generalleave + sickleave 
        data[uid]["projects"]
        context = {
            "project": True,
            "name": name,
            "dep": dep,
            "profile":profile,
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
        return render(request, "rndhome.html", context)
    except:
        context = {
            "project": False,
            "name": name,
            "dep": dep,
            "profile":profile,
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
    return render(request,'rndhome.html',context)
def inprocess(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile = request.COOKIES["profile"]
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
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
    data = db.child("customer").get().val()
    custNameList = []
    custPhnList = []
    for cust in data:
        try:
            if data[cust]["InProcess"]:
                custNameList.append(data[cust]["name"])
                custPhnList.append(cust)
        except:
            pass
    if custNameList == [] and custPhnList == []:
        context = {"nocustomer": "No Customer is currently In Process"}
        return render(request, "rnd/inprocess.html", context)
    # try:
    #     # for cust in data:
    #     #     try:
    #     #         if data[cust]['InProcess']:
    #     #             # custList.append(cust)
    #     #     except:
    #     #         pass
    #     # if data[]
    # except:
    #     pass
    allList = zip(custNameList, custPhnList)
    context = {
        "allList": allList,
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
    return render(request,'inprocess.html',context)

def create(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = request.COOKIES["name"]
    profile = request.COOKIES["profile"]
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
        if not suggestionData[suggestion]["isread"]:
            suggestionNotification += 1
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
        try:
            email1 = request.POST["email"]
            data = shDB.get().val()
            for uid in data:
                try:
                    if email1 in data[uid]["email"]:
                        uidd = data[uid]
                except:
                    pass
            messages.success(request, "User Created for Gate Automation")

        except:
            # try:
            #     email2 = request.POST['email2']
            #     data = shDB.get().val()
            #     for uid in data:
            #         if email1 in data[uid]['email']:
            #     messages.success(request, "User Created for WTA" )
            # except:
            pass
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
    return render(request,'create.html',context)

def gate(request):
    if request.method == "POST":
        if "create-gate" in request.POST:
            _email = request.POST["email"]
            try:
                if request.POST["cycle"]:
                    cycle = True

            except:
                cycle = False
            typ = request.POST["typ"]
            data = shDB.get().val()
            for uid in data:
                try:
                    if _email == data[uid]["email"]:
                        _cycle = cycle
                        gate_type = typ
                        _data = {
                            "Open": True,
                            "Close": True,
                            "Pause": True,
                            "Cycle": _cycle,
                            "Gate_Type": gate_type,
                            "Gate_Status": False,
                            "Single_Gate_Status": False,
                        }
                        shDB.child(uid).update({"Gate": True})
                        shDB.child(uid).child("GateAutomation").child("gate-1").set(_data)
                except:
                    # For Family
                    pass
        if "create-wta" in request.POST:
            _email = request.POST["email"]
            data = shDB.get().val()
            for uid in data:
                try:
                    if _email == data[uid]["email"]:
                        try:
                            if data[uid]["WTA"] == True:
                                context = {"msg":"WaterTankAutomation Already Enabled"}
                                return render(request, "rnd/create.html", context)
                            else:
                                _data = {"level":40, "status":False}
                                shDB.child(uid).update({"WTA": True})
                                shDB.child(uid).child("WaterTankAutomation").child("waterTank1").set(_data)

                        except:
                            pass
                except:
                    pass
    response = redirect(create)
    return response
