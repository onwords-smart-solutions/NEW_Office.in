
from django.contrib import admin
from django.urls import path
from . import views
from it import views as itviews
from pr import views as prviews
from rnd import views as rndviews
from admin import views as adminviews
from superadmin import views as superadminviews
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("leave_form/", views.leave_form, name="leave_form"),
    path("late_form/", views.late_form, name="late_form"),
    path("leaveapproval/", views.leave_approval, name="leave_approval"),
    path("lateapproval/", views.late_approval, name="late_approval"),
    path("suggestion/", views.suggestion, name="suggestion"),
    path("refreshment/",views.refreshment, name="refreshment"),
    path("submitwork/", views.submitwork, name="submitwork"),
    path("editworkdone/", views.editworkdone, name="editworkdone"),
    path("submitaction/", views.submitaction, name="submitaction"),
    path("todo/", views.todo, name="todo"),
    path("approvalprocess/", views.approvalprocess, name="approvalprocess"),

    # ========================coo page =========================

    path('coohome/', views.coohome,name='coohome'),
    path('installation_details',views.installation_details,name='installation_details'),


    path("logout/", views.logout, name="logout"),

    # ============it team================
     path("ithome/", itviews.ithome, name="ithome"),

    # =================pr team============  
    path("prhome/",prviews.prhome,name='prhome'), 
    path("create_lead/",prviews.create_lead,name='create_lead'), 
    path("customer_details/",prviews.customer_details,name='customer_details'), 
    path("points_workdone/",prviews.points_workdone,name='points_workdone'), 
    path("quotation/",prviews.quotation,name='quotation'), 
    path("leadinfo/",prviews.leadinfo,name='leadinfo'), 

    # ================ accounts department ====================

    path("financial/",views.financial,name='financial'),

    # ========== rnd department =================================

    path("rndhome",rndviews.rndhome,name='rndhome'),
    path("inprocess",rndviews.inprocess,name='inprocess'),
    path("create",rndviews.create,name='create'),

    
    # ==================admin department==================================

    path("adminhome",adminviews.adminhome,name='adminhome'),
    path("checkin",adminviews.checkin,name='checkin'),
    path("attendanced",adminviews.attendanced,name='attendanced'),


    # =====================super admin====================================

    path("superadmin",superadminviews.superadmin,name='superadmin'),
    path("createstaff",superadminviews.createstaff,name='createstaff'),
    path("staffaccess",superadminviews.staffaccess,name='staffaccess'),

   
]
