from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("main/", views.company_main, name="company_main"),
    path("register/", views.register, name="company_register"),
    path("company/signin/", views.singin, name="company_signin"),
    path("company/private/", views.company_private, name="company_main"),
    path("company/vacancy/detail/<int:pk>", views.company_vacancy, name="company_vacancy"),
    path("company/student/detail/<int:pk>/vacancy/<int:id>", views.student_detail, name="student_detail"),
    path("company/student/accept/<int:pk>/vacancy/<int:id>",views.accept_vacancy,name="accept_vacancy")
]
