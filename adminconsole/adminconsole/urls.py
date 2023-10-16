
from django.contrib import admin
from django.urls import path
from . import views
from it import views as itviews
from pr import views as prviews
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("leave_form", views.leave_form, name="leave_form"),
    path("late_form", views.late_form, name="late_form"),
    path("approval", views.leave_approval, name="leave_approval"),
    path("lateentry/", views.lateentry, name="lateentry"),
    path("suggestion", views.suggestion, name="suggestion"),
    path("refreshment/",views.refreshment, name="refreshment"),
    path("submitwork/", views.submitwork, name="submitwork"),
    path("editworkdone/", views.editworkdone, name="editworkdone"),

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


    # ================accounts department ====================

    path("financial/",views.financial,name='financial'),

    # ======= CMO Product Page ==========
      path("cmoproduct/",views.cmoproduct,name='cmoproduct'),
]
