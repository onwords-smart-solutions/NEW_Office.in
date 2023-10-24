
from django.contrib import admin
from django.urls import path
from . import views
from it import views as itviews
from pr import views as prviews
from rnd import views as rndviews
from admin import views as adminviews
from superadmin import views as superadminviews
from hr import views as hrviews
from installation import views as installationviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("leave_form/", views.leave_form, name="leave_form"),
    path("late_form/", views.late_form, name="late_form"),
    path("leaveapproval/", views.leave_approval, name="leave_approval"),
    path("lateapproval/", views.late_approval, name="late_approval"),
    path("approval/",views.approval,name='approval'),
    path("suggestion/", views.suggestion, name="suggestion"),
    path("refreshment/",views.refreshment, name="refreshment"),
    path("submitwork/", views.submitwork, name="submitwork"),
    path("editworkdone/", views.editworkdone, name="editworkdone"),
    path("submitaction/", views.submitaction, name="submitaction"),
    path("todo/", views.todo, name="todo"),
    path("approvalprocess/", views.approvalprocess, name="approvalprocess"),
    path("financialpost/",views.financialpost,name="financialpost"),
    path("attendancesort/",adminviews.attendancesort,name="attendancesort"),
    path("logout/",views.logout,name="logout"),
    path("workdonedetails/",views.workdonedetails,name="workdonedetails"),
    path("workmanagerTl/",views.workmanagerTl,name='workmanagreTl'),

    # ========================coo page =========================

    path('prdashboard/',views.prdashboard,name='pradshboard'),
    path('coohome/', views.coohome,name='coohome'),
    path('installation_details/',views.installation_details,name='installation_details'),

    # ============it team================
     path("ithome/", itviews.ithome, name="ithome"),

    # =================pr team============  
    path("prhome/",prviews.prhome,name='prhome'), 
    path("create_lead/",prviews.create_lead,name='create_lead'), 
    path("customer_details/",prviews.customer_details,name='customer_details'), 
    path("points_workdone/",prviews.points_workdone,name='points_workdone'), 
    path("quotation/",prviews.quotation,name='quotation'),
    path("invoiceForm/", prviews.invoiceForm, name="invoiceForm"),
    path("pinvoiceForm/", prviews.pinvoiceForm, name="pinvoiceForm"),
    path("quoteForm/", prviews.quoteForm, name="quoteForm"),
    path("leadinfo/",prviews.leadinfo,name='leadinfo'),
    
    path("leadinfo/",prviews.leadinfo,name="leadinfo"),
    path("addnotes/",prviews.addnotes,name="addnotes"),
    # ================ accounts department ====================

    path("financial/",views.financial,name='financial'),

    # ========== rnd department =================================

    path("rndhome/",rndviews.rndhome,name='rndhome'),
    path("inprocess/",rndviews.inprocess,name='inprocess'),
    path("create/",rndviews.create,name='create'),
    path("gate/",rndviews.gate,name='gate'),

    # ==================admin department==================================
    
    path("adminhome/",adminviews.adminhome,name='adminhome'),
    path("checkin/",adminviews.checkin,name='checkin'),
    path("attendanced/",adminviews.attendanced,name='attendanced'),
    path("indvattendanced/",adminviews.indvattendanced,name='indvattendanced'),

    # ======= CMO Product Page ==========
    path("inventorymanagement/",views.inventorymanagement,name='inventorymanagement'),

    # =====================super admin====================================

    path("superadmin/",superadminviews.superadmin,name='superadmin'),
    path("createstaff/",superadminviews.createstaff,name='createstaff'),
    path("staffaccess/",superadminviews.staffaccess,name='staffaccess'),
    path("userdata/",views.userdata,name='userdata'),
    path("viewsuggestion/",superadminviews.viewsuggestion,name='viewsuggestion'),
    path("viewworkmanager/",superadminviews.viewworkmanager,name='viewworkmanager'),
    path("markasread/", superadminviews.markasread, name="markasread"),

    # =====================hr====================================
    path("hrhome/",hrviews.hrhome,name='hrhome'),
   

    # =====================installation ====================================
    path("installationhome/",installationviews.installationhome,name='installationhome'),
    path("installationadd/",installationviews.installationadd,name='installationadd'),
]