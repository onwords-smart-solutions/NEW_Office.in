from django.shortcuts import render, redirect
from adminconsole.views import db, checkUserName
from adminconsole.views import checkUserDepartment
from adminconsole.views import db, storage
from datetime import date,datetime, timedelta
import csv, codecs
from it.views import convert_to_12_hour_format,calculate_progress,calculate_progress_
from django.http import HttpResponse
# Create your views here.

def prhome(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    data = db.child("staff").get().val()
    attendence = db.child("attendance").get().val()
    workmanager = db.child("workmanager").get().val()
    leavedetails = db.child("leaveDetails").get().val()
    name = checkUserName(uid)
    istl = False
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
    try:
        try:
            print("==")
            print("date", current_year, current_month, current_day, uid)
            todaycheckin = attendence[current_year][current_month][current_day][uid]["check_in"]
            
            print("today", todaycheckin)
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
                yesscheckout = convert_to_12_hour_format(yescheckin)
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
            print("progress", yesterdayprogress)
        except:
            yesterdayprogress = "Absent"    
        try:
            today_progress= calculate_progress_(todaycheckin, todaycheckout)
            print("prog",today_progress)
        except:
            today_progress= "Absent"
        todaycheckout = convert_to_12_hour_format(todaycheckout)
        todaycheckin = convert_to_12_hour_format(todaycheckin)   

        listOfTodaysWork= []
        print("date",formatted_date)
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
            leavedata = db.child("leaveDetails").get().val()
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
                # "suggestionNotification":suggestionNotification
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
            "tl": istl,
            "dep": dep,
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
        }
        return render(request, "prhome.html", context)
    except:
        context = {
            "project": False,
            "name": name,
            "tl": istl,
            "dep": dep,
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
        }
    return render(request, "prhome.html", context)

def create_lead(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    logedInUser = request.COOKIES["uid"]
    loginState = request.COOKIES["loginState"]
    alreadyExistList = []
    custData = db.child("customer").get().val()
    name = checkUserName(uid)
    staff_data = db.child("staff").get().val()
    uid_list=[] 
    nameList = []    
    for uid in staff_data:
        if staff_data[uid]['department'] == "PR":
            uid_list.append(uid)
            nameList.append(staff_data[uid]['name'])
    # istl = False
    # praproval = False
    # tl = db.child("tl").get().val()
    # for t in tl:
    #     if name == tl[t]:
    #         istl = True
    #         break
    # accounts = False
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
    #     accounts = True
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" or uid == 'yleZdWDZgFYTBxwzC5NtHVeb3733' or uid == 'jDYzpwcpv3akKaoDL9N4mllsGCs2':
    #     praproval = True    
    # management = False
    # if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2":
    #     management = True    
    if loginState == "loggedIn":
        try:
            if request.method == "POST":
                if "create-using-data" in request.POST:
                    data = db.get().val()
                    phno = request.POST["phn"]
                    for cust in data["customer"]:
                        if phno == cust:
                            return render(request,"createLead.html", {"error": "Phone number already exist in customer list","nameList":nameList})
                    for dcust in data["deletedcustomers"]:
                        if phno == dcust:
                            return render(request,"createLead.html", {"error": "Phone number already exist in deleted customers list","nameList":nameList})
                    name = request.POST["name"]
                    if len(phno) < 10:
                        return render(request,"createLead.html",{"error": "phone number should not be less the 10 digit","nameList":nameList})
                    city = request.POST["city"]
                    try:
                        Email = request.POST["email"]
                    except:
                        Email = "Not Found"
                    dfb = request.POST["dfb"]
                    curent_date = date.today()
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    ef = request.POST["ef"]
                    data = {
                        "name": name,
                        "phone_number": phno,
                        "city": city,
                        "email_id": Email,
                        "data_fetched_by": dfb,
                        "LeadIncharge": "Not Assigned",
                        "rating": 0,
                        "created_time": current_time,
                        "created_date": str(curent_date),
                        "inquired_for": ef,
                        "created_by": checkUserName(uid),
                        "customer_state": "New leads",
                    }
                
                    db.child("customer").child(phno).set(data)
                    return render(
                        request,
                        "createLead.html",
                        {"akn": "user created success fully", "colour": True,"nameList":nameList},
                    )
                print("method",request.POST)
                if "create-using-file" in request.POST:
                    print("==")
                    curent_date = date.today()
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    enqFor = request.POST["eqfor"]
                    print("for",enqFor)
                    name = request.POST["selectedName"]
                    print("name",name)
                    # selected_staffs = request.POST.getlist('selectedStaffs')
                    reader=request.FILES['myfile']
                    
                    a=0
                    read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
                    for row in read:
                        if any(field.strip() for field in row):
                            name = row[0]
                            original_phone_number = row[1]
                            email = row[2]
                            city = row[3]
                            altered_phone_number = original_phone_number.replace(" ", "")
                            if len(altered_phone_number)>10:
                                if "p:" in altered_phone_number:
                                    altered_phone_number = altered_phone_number.replace("p:","")
                                if len(altered_phone_number) >= 13 and "+91" in altered_phone_number:
                                    altered_phone_number = altered_phone_number.replace("+91","")
                                if len(altered_phone_number) >= 12 and "+1" in altered_phone_number:
                                    altered_phone_number = altered_phone_number.replace("+1","")
                                if len(altered_phone_number) >= 12 and "+78" in altered_phone_number:
                                    altered_phone_number = altered_phone_number.replace("+78","")
                                if altered_phone_number[0] == "0":
                                    altered_phone_number = altered_phone_number.replace("0", "", 1)

                            if len(altered_phone_number) == 10:
                                number = altered_phone_number
                            else:
                                number = original_phone_number
                            cust_data = {
                                "name": name,
                                "phone_number": number,
                                "city": city,
                                "email_id": email,
                                "data_fetched_by": "Facebook Ads",
                                "LeadIncharge": "Not Assigned",
                                "created_by": checkUserName(logedInUser),
                                "created_by": name,
                                "created_date": str(curent_date),
                                "created_time": current_time,
                                "customer_state": "New leads",
                                "inquired_for": enqFor,
                                "rating": 0
                            }
                            # custData = db.child("customer").get().val()
                            # if number not in custData:
                            #     db.child("customer").child(number).update(cust_data)
                            # else:
                            #     alreadyExistList.append(number)
                            try:
                                custData[number]
                                alreadyExistList.append(number)
                            except Exception as err:
                                db.child("customer").child(number).update(cust_data)
                            # return render(request,"pr/createlead.html",{"akn": "user created success fully", "colour": True, "tl":istl, "accounts": accounts,"management": management,"alreadyExistList": alreadyExistList})
                            # db.child("customer").child(number).update(cust_data)
                        else:
                            pass    
                    return render(request, "createLead.html", {"akn": "user created success fully", "colour": True, "alreadyExistList": alreadyExistList,"nameList":nameList})
            else:
                return render(request,"createLead.html",{"akn": "error creating user", "colour": False,"alreadyExistList": alreadyExistList,"nameList":nameList})
        except:
            return render(request,"createLead.html",{"akn": "error creating user", "colour": False,"alreadyExistList": alreadyExistList,"nameList":nameList})

    else:
        return redirect("login")

def customer_details(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    # istl = False
    # praproval = False
    
    # tl = db.child("tl").get().val()
    # for t in tl:
    #     if name == tl[t]:
    #         istl = True
    #         break
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" or uid== "jDYzpwcpv3akKaoDL9N4mllsGCs2":
    #     praproval = True    
   
    # accounts = False
    # suggestionNotification = 0
    # suggestionData = db.child("suggestion").get().val()
    # for suggestion in suggestionData:
    #         if not suggestionData[suggestion]["isread"]:
    #             suggestionNotification += 1
    # if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2":
    #     accounts = True
    # management = False
    # if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2":
    #     management = True    
    data = db.child("customer").get().val()
    customerNameList, customerPhoneList, customerStateList, customerCreatedList, lastNoteList, lastNoteDateList, leadInchargeList = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )
    (
        followUpCount,
        delayedCount,
        onwordsCount,
        advancedCount,
        b2bCount,
        productCount,
        ucCount,
        installationCompletedCount,
        totalCount,
        othersCount,
        interestedCount,
        newleadscount
    ) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for cust in data:
        try:
            customerNameList.append(data[cust]["name"])
            customerPhoneList.append(data[cust]["phone_number"])
            customerStateList.append(data[cust]["customer_state"])
            customerCreatedList.append(data[cust]["created_date"])
            totalCount += 1
        except:
            print(cust)
            pass
        try:
            data[cust]["notes"]
            for note in data[cust]["notes"]:
                lastNote = data[cust]["notes"][note]["note"]
                lastNoteDate = data[cust]["notes"][note]["date"]
            lastNoteList.append(lastNote)
            lastNoteDateList.append(lastNoteDate)
        except:
            lastNoteList.append("No Notes were found")
            lastNoteDateList.append("-")
        try:
            data[cust]["LeadIncharge"]
            leadInchargeList.append(data[cust]["LeadIncharge"])
        except:
            leadInchargeList.append("Lead Incharge Not Assigned")
        cusState = data[cust]["customer_state"]
        if cusState == "Following Up":
            followUpCount += 1
        if cusState == "Delayed":
            delayedCount += 1
        if cusState == "Rejected from Customer end":
            onwordsCount += 1
        if cusState == "Rejected from Customer":
            onwordsCount += 1
        if cusState == "Rejected from MGMT":
            onwordsCount += 1
        if cusState == "Rejected from management side":
            onwordsCount += 1
        if cusState == "Onwords":
            onwordsCount += 1
        if cusState == "Advanced":
            advancedCount += 1
        if cusState == "Installation Completed":
            installationCompletedCount += 1
        if cusState == "B2B":
            b2bCount += 1
        if cusState == "Product":
            productCount += 1
        if cusState == "Under Construction":
            ucCount += 1
        if cusState == "Hot lead" or cusState == "Interested":
            interestedCount += 1
        if cusState == "New leads":
            newleadscount +=1
        

        allList = [
            "Following Up",
            "Delayed",
            "Rejected from Customer end",
            "Rejected from management side",
            "Advanced",
            "Product",
            "Installation Completed",
            "Rejected from Customer",
            "Rejected from MGMT",
            "Hot lead",
            "B2B",
            "Under Construction",
            "Onwords",
            "Interested",
            "newleadscount"
        ]
        if cusState not in allList:
            othersCount += 1
    allData = zip(
        customerNameList,
        customerPhoneList,
        customerStateList,
        lastNoteList,
        lastNoteDateList,
        leadInchargeList,
        customerCreatedList,
    )
    allDataMob = zip(
        customerNameList,
        customerPhoneList,
        customerStateList,
        lastNoteList,
        lastNoteDateList,
        leadInchargeList,
        customerCreatedList,
    )

    context = {
        "name": name,
        "allData": allData,
        "allDataMob": allDataMob,
        "followUpCount": followUpCount,
        "delayedCount": delayedCount,
        "onwordsCount": onwordsCount,
        "advancedCount": advancedCount,
        "b2bCount": b2bCount,
        "productCount": productCount,
        "ucCount": ucCount,
        "installationCompletedCount": installationCompletedCount,
        "totalCount": totalCount,
        "othersCount": othersCount,
        "interestedCount":interestedCount,
        "newleadscount":newleadscount,
        "dep": dep,
        # "tl": istl,
        # "accounts": accounts,
        # "management": management,
        # "suggestionNotification":suggestionNotification,
        # "praproval":praproval,
        
    }
    return render(request, "customer_details.html", context)
def points_workdone(request):
    return render(request,'points_workdone.html')
def quotation(request):
    if request.method =="POST":
        date1=request.POST["get-total1"]
        uid = request.COOKIES["uid"]
        dep = request.COOKIES["dep"]
        name = checkUserName(uid)
        istl = False
        tl = db.child("tl").get().val()
        for t in tl:
            if name == tl[t]:
                istl = True
                break
        suggestionNotification = 0
        suggestionData = db.child("suggestion").get().val()
        for suggestion in suggestionData:
                if not suggestionData[suggestion]["isread"]:
                    suggestionNotification += 1
        # todaysDate = str(date.today())
        todaysDate=str(date1)
        thisYear = todaysDate[:4]
        thisMonth = todaysDate[5:7]
        quote = db.child("QuotationAndInvoice").get().val()
        cust = db.child("customer").get().val()
        iNum, iCreatedBy, iTimeStampDate,iTimeStampTime, idocument_link, imobile_number, iNameList = [], [], [], [], [], [], []
        piNum,piCreatedBy,piTimeStampDate,piTimeStampTime,pidocument_link,piinstallation_document_link,pimobile_number,piNameList =[], [], [], [], [], [], [], []
        qNum, qCreatedBy,qTimeStampDate,qTimeStampTime, qdocument_link, qmobile_number, qNameList = [], [], [], [], [], [], []
        ilastNoteList,ilastNoteDateList,pilastNoteList,pilastNoteDateList, qlastNoteList, qlastNoteDateList = [], [], [], [], [], []
        invoice = quote["INVOICE"][thisYear]
        pinvoice = quote["PROFORMA_INVOICE"][thisYear]
        _quotation = quote["QUOTATION"][thisYear]
        # for _time in invoice:
        #   ts = invoice[_time]['TimeStamp']
        #   timeList.append(datetime.fromtimestamp(ts))
        #   )
        # timeList.sort()
        # timeCount = 0
        for inv_num in invoice[thisMonth]:
            # if invoice[inv_num]['TimeStamp'][timeList[timeCount]]:
            iNum.append(inv_num)
            iCreatedBy.append((invoice[thisMonth][inv_num]["CreatedBy"].split("@")[0]).capitalize())
            ts = invoice[thisMonth][inv_num]["TimeStamp"]
            try:
                datecon=str(datetime.fromtimestamp(ts)).split()[0]
                if datecon == todaysDate:
                    iTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                    iTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                datecon=str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0]
                if datecon == todaysDate:
                    iTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                    iTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            idocument_link.append(invoice[thisMonth][inv_num]["document_link"])
            imobile_number.append(invoice[thisMonth][inv_num]["mobile_number"])
        for number in imobile_number:
            try:
                iNameList.append(cust[str(number)]["name"])
            except:
                iNameList.append("Customer not in our lead list")


        for pinv_num in pinvoice[thisMonth]:
            # if invoice[inv_num]['TimeStamp'][timeList[timeCount]]:
            piNum.append(inv_num)
            piCreatedBy.append((pinvoice[thisMonth][pinv_num]["CreatedBy"].split("@")[0]).capitalize())
            ts = pinvoice[thisMonth][pinv_num]["TimeStamp"]
            try:
                datecon=str(datetime.fromtimestamp(ts)).split()[0]
                if datecon == todaysDate:
                    piTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                    piTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                datecon=str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0]
                if datecon == todaysDate:
                    piTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                    piTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            pidocument_link.append(pinvoice[thisMonth][pinv_num]["document_link"])
            piinstallation_document_link.append(pinvoice[thisMonth][pinv_num]["installation_document_link"])
            pimobile_number.append(pinvoice[thisMonth][pinv_num]["mobile_number"])
        for pnumber in pimobile_number:
            try:
                piNameList.append(cust[str(pnumber)]["name"])
            except:
                piNameList.append("Customer not in our lead list")

       
        for quote_num in _quotation[thisMonth]:
            qNum.append(quote_num)
            try:
                qCreatedBy.append((_quotation[thisMonth][quote_num]["CreatedBy"].split("@")[0]).capitalize())
            except:
                pass
            ts = _quotation[thisMonth][quote_num]["TimeStamp"]
            try:
                datecon1=str(datetime.fromtimestamp(ts)).split()[0]
                if datecon1 == todaysDate:
                    qTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                    qTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                datecon1=str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0]
                if datecon1 == todaysDate:
                    qTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                    qTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            qdocument_link.append(_quotation[thisMonth][quote_num]["document_link"])
            qmobile_number.append(_quotation[thisMonth][quote_num]["mobile_number"])
        for number in qmobile_number:
            try:
                qNameList.append(cust[str(number)]["name"])
            except:
                qNameList.append("Customer not in our lead list")

        for num in imobile_number:
            num = str(num)
            try:
                cust[num]["notes"]
                for note in cust[num]["notes"]:
                    lastNote = cust[num]["notes"][note]["note"]
                    lastNoteDate = cust[num]["notes"][note]["date"]
                ilastNoteList.append(lastNote)
                ilastNoteDateList.append(lastNoteDate)
            except:
                ilastNoteList.append("No Notes were found")
                ilastNoteDateList.append("-")

        for pnum in pimobile_number:
            pnum = str(pnum)
            try:
                cust[pnum]["notes"]
                for note in cust[pnum]["notes"]:
                    lastNote = cust[pnum]["notes"][note]["note"]
                    lastNoteDate = cust[pnum]["notes"][note]["date"]
                pilastNoteList.append(lastNote)
                pilastNoteDateList.append(lastNoteDate)
            except:
                pilastNoteList.append("No Notes were found")
                pilastNoteDateList.append("-")


        for num in qmobile_number:
            num = str(num)
            try:
                cust[num]["notes"]
                for note in cust[num]["notes"]:
                    lastNote = cust[num]["notes"][note]["note"]
                    lastNoteDate = cust[num]["notes"][note]["date"]
                qlastNoteList.append(lastNote)
                qlastNoteDateList.append(lastNoteDate)
            except:
                qlastNoteList.append("No Notes were found")
                qlastNoteDateList.append("-")

        invoiceList = zip(iNameList,imobile_number,iCreatedBy,iNum,iTimeStampDate,iTimeStampTime,idocument_link,ilastNoteList,ilastNoteDateList)
        pinvoiceList = zip(piNameList,pimobile_number,piCreatedBy,piNum,piTimeStampDate,piTimeStampTime,pidocument_link,piinstallation_document_link,pilastNoteList,pilastNoteDateList)
        quotationList = zip(qNameList,qmobile_number,qCreatedBy,qNum,qTimeStampDate,qTimeStampTime,qdocument_link,qlastNoteList,qlastNoteDateList)
        invoiceListMobile = zip(iNameList,imobile_number,iCreatedBy,iNum,iTimeStampDate,iTimeStampTime, idocument_link,ilastNoteList,ilastNoteDateList)
        pinvoiceListMobile = zip(piNameList,pimobile_number,piCreatedBy,piNum,piTimeStampDate,piTimeStampTime,pidocument_link,pilastNoteList,pilastNoteDateList) 
        quotationListMobile = zip(qNameList,qmobile_number,qCreatedBy,qNum,qTimeStampDate,qTimeStampTime,qdocument_link,qlastNoteList,qlastNoteDateList)
        context = {
            "invoiceList": invoiceList,
            "pinvoiceList": pinvoiceList,
            "quotationList": quotationList,
            "invoiceListMobile": invoiceListMobile,
            "pinvoiceListMobile" : pinvoiceListMobile,
            "quotationListMobile": quotationListMobile,
            "dep": dep,
            "tl": istl,
            "suggestionNotification":suggestionNotification
        }
        # iTimeStamp.sort()
        # qTimeStamp.sort()
        return render(request, "superadmin/quotation.html", context)


    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    istl = False
    tl = db.child("tl").get().val()
    for t in tl:
        if name == tl[t]:
            istl = True
            break
    suggestionNotification = 0
    suggestionData = db.child("suggestion").get().val()
    for suggestion in suggestionData:
            if not suggestionData[suggestion]["isread"]:
                suggestionNotification += 1
    todaysDate = str(date.today())
    thisYear = todaysDate[:4]
    thisMonth = todaysDate[5:7]
    quote = db.child("QuotationAndInvoice").get().val()
    cust = db.child("customer").get().val()
    iNum, iCreatedBy, iTimeStampDate,iTimeStampTime, idocument_link, imobile_number, iNameList = [], [], [], [], [], [], []
    piNum,piCreatedBy,piTimeStampDate,piTimeStampTime,pidocument_link,piinstallation_document_link,pimobile_number,piNameList =[], [], [], [], [], [], [], []
    qNum, qCreatedBy,qTimeStampDate,qTimeStampTime, qdocument_link, qmobile_number, qNameList = [], [], [], [], [], [], []
    ilastNoteList,ilastNoteDateList,pilastNoteList,pilastNoteDateList, qlastNoteList, qlastNoteDateList = [], [], [], [], [], []
    invoice = quote["INVOICE"][thisYear]
    _quotation = quote["QUOTATION"][thisYear]
    pinvoice = quote["PROFORMA_INVOICE"][thisYear]
    # for _time in invoice:
    #   ts = invoice[_time]['TimeStamp']
    #   timeList.append(datetime.fromtimestamp(ts))
    #   )
    # timeList.sort()
    # timeCount = 0
    for month in invoice:
        for inv_num in invoice[month]:
            # if invoice[inv_num]['TimeStamp'][timeList[timeCount]]:
            iNum.append(inv_num)
            iCreatedBy.append((invoice[month][inv_num]["CreatedBy"].split("@")[0]).capitalize())
            ts = invoice[month][inv_num]["TimeStamp"]
            try:
                iTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                iTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                iTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                iTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            idocument_link.append(invoice[month][inv_num]["document_link"])
            imobile_number.append(invoice[month][inv_num]["mobile_number"])
    for number in imobile_number:
        try:
            iNameList.append(cust[str(number)]["name"])
        except:
            iNameList.append("Customer not in our lead list")

    for month in pinvoice:
        for pinv_num in pinvoice[month]:
            # if invoice[inv_num]['TimeStamp'][timeList[timeCount]]:
            piNum.append(pinv_num)
            piCreatedBy.append((pinvoice[month][pinv_num]["CreatedBy"].split("@")[0]).capitalize())
            ts = pinvoice[month][pinv_num]["TimeStamp"]
            try:
                piTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                piTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                piTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                piTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            pidocument_link.append(pinvoice[month][pinv_num]["document_link"])
            piinstallation_document_link.append(pinvoice[month][pinv_num]["installation_document_link"])
            pimobile_number.append(pinvoice[month][pinv_num]["mobile_number"])
    for number in pimobile_number:
        try:
            piNameList.append(cust[str(number)]["name"])
        except:
            piNameList.append("Customer not in our lead list")
    for month in _quotation:
        for quote_num in _quotation[month]:
            qNum.append(quote_num)
            try:
                qCreatedBy.append((_quotation[month][quote_num]["CreatedBy"].split("@")[0]).capitalize())
            except:
                pass
            ts = _quotation[month][quote_num]["TimeStamp"]
            try:
                qTimeStampDate.append(str(datetime.fromtimestamp(ts)).split()[0])
                qTimeStampTime.append(str(datetime.fromtimestamp(ts)).split()[1])
            except:
                qTimeStampDate.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[0])
                qTimeStampTime.append(str(datetime.fromtimestamp(ts / 1000).replace(microsecond=0)).split()[1])
            qdocument_link.append(_quotation[month][quote_num]["document_link"])
            qmobile_number.append(_quotation[month][quote_num]["mobile_number"])
    for number in qmobile_number:
        try:
            qNameList.append(cust[str(number)]["name"])
        except:
            qNameList.append("Customer not in our lead list")
    for num in imobile_number:
        num = str(num)
        try:
            cust[num]["notes"]
            for note in cust[num]["notes"]:
                lastNote = cust[num]["notes"][note]["note"]
                lastNoteDate = cust[num]["notes"][note]["date"]
            ilastNoteList.append(lastNote)
            ilastNoteDateList.append(lastNoteDate)
        except:
            ilastNoteList.append("No Notes were found")
            ilastNoteDateList.append("-")

    for pnum in pimobile_number:
            pnum = str(pnum)
            try:
                cust[pnum]["notes"]
                for note in cust[pnum]["notes"]:
                    lastNote = cust[pnum]["notes"][note]["note"]
                    lastNoteDate = cust[pnum]["notes"][note]["date"]
                pilastNoteList.append(lastNote)
                pilastNoteDateList.append(lastNoteDate)
            except:
                pilastNoteList.append("No Notes were found")
                pilastNoteDateList.append("-")    

    for num in qmobile_number:
        num = str(num)
        try:
            cust[num]["notes"]
            for note in cust[num]["notes"]:
                lastNote = cust[num]["notes"][note]["note"]
                lastNoteDate = cust[num]["notes"][note]["date"]
            qlastNoteList.append(lastNote)
            qlastNoteDateList.append(lastNoteDate)
        except:
            qlastNoteList.append("No Notes were found")
            qlastNoteDateList.append("-")
    invoiceList = zip(iNameList,imobile_number,iCreatedBy,iNum,iTimeStampDate,iTimeStampTime,idocument_link,ilastNoteList,ilastNoteDateList)
    pinvoiceList = zip(piNameList,pimobile_number,piCreatedBy,piNum,piTimeStampDate,piTimeStampTime,pidocument_link,piinstallation_document_link,pilastNoteList,pilastNoteDateList)
    quotationList = zip(qNameList,qmobile_number,qCreatedBy,qNum,qTimeStampDate,qTimeStampTime,qdocument_link,qlastNoteList,qlastNoteDateList)
    invoiceListMobile = zip(iNameList,imobile_number,iCreatedBy,iNum,iTimeStampDate,iTimeStampTime, idocument_link,ilastNoteList,ilastNoteDateList)
    pinvoiceListMobile = zip(piNameList,pimobile_number,piCreatedBy,piNum,piTimeStampDate,piTimeStampTime,pidocument_link,pilastNoteList,pilastNoteDateList) 
    quotationListMobile = zip(qNameList,qmobile_number,qCreatedBy,qNum,qTimeStampDate,qTimeStampTime,qdocument_link,qlastNoteList,qlastNoteDateList)
    context = {
        "invoiceList": invoiceList,
        "pinvoiceList": pinvoiceList,
        "quotationList": quotationList,
        "invoiceListMobile": invoiceListMobile,
        "pinvoiceListMobile" : pinvoiceListMobile,
        "quotationListMobile": quotationListMobile,
        "dep": dep,
        "tl": istl,
        "suggestionNotification":suggestionNotification
    }
    # iTimeStamp.sort()
    # qTimeStamp.sort()
    return render(request, "superadmin/quotation.html", context)

    return render(request,'quotation.html')
def leadinfo(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    istl = False
    tl = db.child("tl").get().val()
    for t in tl:
        if name == tl[t]:
            istl = True
            break
    accounts = False
    if uid == "tQYuqy2ma6ecGURWSMpmNeVCHiD2" or uid == "jDYzpwcpv3akKaoDL9N4mllsGCs2":
        accounts = True
    management = False
    if uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2" or uid == "ZIuUpLfSIRgRN5EqP7feKA9SbbS2"or uid=="jDYzpwcpv3akKaoDL9N4mllsGCs2":
        management = True    

    try:
        a = request.POST["numb"]
    except:
        a = request.COOKIES["userPhno"]
    userData = db.child("customer").get().val()
    try:
        allData = userData[a]
    except:
        return HttpResponse("<h1>User not found</h1>")
    notesList = []
    schedulesList = []
    try:
        notes = userData[a]["notes"]
        for n in notes:
            notesList.append(notes[n])
    except:
        pass
    try:
        incharge = userData[a]["LeadIncharge"]
    except:
        incharge = "Assign an incharge to this customer"
    try:
        clientData = userData[a]
        star = int(clientData["rating"])
        if star == 0:
            starData = {
                "one": False,
                "two": False,
                "three": False,
                "four": False,
                "five": False,
            }
        elif star == 1:
            starData = {
                "one": True,
                "two": False,
                "three": False,
                "four": False,
                "five": False,
            }
        elif star == 2:
            starData = {
                "one": False,
                "two": True,
                "three": False,
                "four": False,
                "five": False,
            }
        elif star == 3:
            starData = {
                "one": False,
                "two": False,
                "three": True,
                "four": False,
                "five": False,
            }
        elif star == 4:
            starData = {
                "one": False,
                "two": False,
                "three": False,
                "four": True,
                "five": False,
            }
        elif star == 5:
            starData = {
                "one": False,
                "two": False,
                "three": False,
                "four": False,
                "five": True,
            }
        else:
            pass
    except:
        pass
    try:
        schedules = userData[a]["schedules"]
        for s in schedules:
            schedulesList.append(schedules[s])
    except:
        pass
    uid = request.COOKIES["uid"]
    if uid == "ZIuUpLfSIRgRN5EqP7feKA9SbbS2" or uid == "ujUtXFPW91NWQ17UZiLQ5aI7FtD2" or uid == "aOHbaMFpmMM4dB87wFyRVduAX7t2" or uid=="jDYzpwcpv3akKaoDL9N4mllsGCs2":
        context = {
            "userData": allData,
            "notesData": notesList,
            "star": starData,
            "schedulesData": schedulesList,
            "incharge": incharge,
            "management": True,
            "tl":istl,
            "dep":dep,
            "accounts":accounts,
            "management":management
        }
    else:
        context = {
            "userData": allData,
            "notesData": notesList,
            "star": starData,
            "schedulesData": schedulesList,
            "incharge": incharge,
            "tl":istl,
            "dep":dep,
            "accounts":accounts,
            "management":management
        }
    response = render(request, "leadinfo.html", context)
    response.set_cookie("userPhno", a)
    return response

def addnotes(request):
    uid = request.COOKIES["uid"]
    name = checkUserName(uid)
    nts = request.POST["nts"]
    phn = request.COOKIES["userPhno"]
    currDate = str(date.today())
    currTime = datetime.now().strftime("%H:%M")
    notes = {
        "date": currDate,
        "time": currTime,
        "note": nts,
        "entered_by": name,
    }
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    db.child("customer").child(phn).child("notes").child(curr_time).set(notes)
    return redirect(leadinfo)

def approval(request):
    return render(request,'approval.html')

def checkUserName(uid):
    data = db.child("staff").get().val()
    for x in data:
        if uid == x:
            z = data[x]["name"]
            return z