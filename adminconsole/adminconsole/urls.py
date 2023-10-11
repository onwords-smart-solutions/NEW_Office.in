
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
    path("suggestion", views.suggestion, name="suggestion"),



    # ============it team===============
     path("ithome/", itviews.ithome, name="ithome"),

    # =================pr team============  
    path("prhome/",prviews.prhome,name='prhome'), 
    path("create_lead/",prviews.create_lead,name='create_lead') 
]
