from django.shortcuts import render
from adminconsole.views import db, checkUserName
from datetime import datetime, timedelta

# Create your views here.
def adminhome(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    name = checkUserName(uid)
    context = {
        "name":name,
        "dep":dep,
    }
    return render(request,'adminhome.html',context)
def checkin(request):
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
        dates = request.POST.get("date")
    else:
        todaysDate = datetime.today()
        yesterdayDate = todaysDate - timedelta(days=1)
        dates = yesterdayDate.strftime("%Y-%m-%d")

    date_parts = dates.split("-")
    tyear = date_parts[0]
    tmonth = date_parts[1]
    tday = date_parts[2]   

    attend = attendance[tyear][tmonth][tday]
    
    for staff in staffDB:
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
    
    total_staff_count = len(staffDB)
    present_staff_count = total_staff_count - len(absentstaff)
    absent_staff_count = len(absentstaff)

    sorted_finallist = sorted(zip(staffnamelist,attendenceloginlist,attendencelogoutlist,workinghourlist,workinghourlistall,attype,outtype), key=lambda x: x[0])
    absentworkinghourlist = sorted(zip(absentstaff, absentworkinghours), key=lambda x: x[0])

    context = {
        "request": request,
        "finallist": sorted_finallist,
        "absenteeslist":absentworkinghourlist,
        "totalcount":total_staff_count,
        "presentcount":present_staff_count,
        "absentcount":absent_staff_count,
        "date":dates,
    }
    return render(request,'checkin.html',context) 
def attendanced(request):
    return render(request,'attendanced.html')