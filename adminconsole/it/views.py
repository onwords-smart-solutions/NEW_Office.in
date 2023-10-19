from django.shortcuts import render
from adminconsole.views import db, checkUserName
from datetime import datetime, timedelta
import pytz
# Create your views here.
def ithome(request):
    uid = request.COOKIES["uid"]
    dep = request.COOKIES["dep"]
    data = db.child("staff").get().val()
    attendence = db.child("attendance").get().val()
    workmanager = db.child("workmanager").get().val()
    leavedetails = db.child("leaveDetails").get().val()
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
        }
        return render(request, "ithome.html", context)
    except:
        context = {
            "project": False,
            "name": name,
            "tl": istl,
            "dep": dep,
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
        }

    return render(request, "ithome.html", context)
    
def calculate_progress_(today_checkin, today_checkout, goal_hours=9):
    try:
        print("starting")
        asia_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(asia_timezone).strftime('%H:%M:%S')

        if today_checkin != "No Entry":
            today_checkin_time = datetime.strptime(today_checkin, "%H:%M:%S")
            
            if today_checkout == "No Entry":
                today_checkout_time = datetime.strptime(current_time, "%H:%M:%S")
            else:
                today_checkout_time = datetime.strptime(today_checkout, "%H:%M:%S")

            time_difference = today_checkout_time - today_checkin_time
            progress_hours = time_difference.total_seconds() / 3600
            progress_percentage = (progress_hours / goal_hours) * 100
            print("func",progress_percentage)

            return progress_percentage
        else:
            return "No Entry"
    except Exception as e:
        print(f"Error: {e}")
        return "No Entry"
   
def calculate_progress(working_hours, goal_hours=9):
    try:
        # Convert the working_hours to a timedelta object
        working_hours = datetime.strptime(working_hours, "%H:%M:%S").time()

        # Calculate the total working time in seconds
        total_working_seconds = working_hours.hour * 3600 + working_hours.minute * 60 + working_hours.second

        # Calculate progress as a percentage
        progress_percentage = min(100, (total_working_seconds / (goal_hours * 3600)) * 100)

        return progress_percentage
    except:
        return "Absent"    

def convert_to_12_hour_format(progress):
    try:
        time_24h_obj = datetime.strptime(progress, "%H:%M:%S")
        time_12h = time_24h_obj.strftime("%I:%M %p")
    except:
        time_12h = "No Entry"    
    return time_12h


