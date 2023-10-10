
from django.contrib import admin
from django.urls import path
from . import views
from it import views as itviews
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("leave_form", views.leave_form, name="leave_form"),
    path("late_form", views.late_form, name="late_form"),



    # ============it team===============
     path("ithome/", itviews.ithome, name="ithome"),
]
