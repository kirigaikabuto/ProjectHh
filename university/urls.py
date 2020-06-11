
from django.urls import path
from . import views
urlpatterns = [
   path("login/",views.studentLogin,name="studentLogin"),
   path("private/",views.studentMain,name="studentPrivate"),
   path("logout/",views.userLogout,name="userLogout"),
   path("private/profile/",views.studentProfile,name="studentProfile"),
]
