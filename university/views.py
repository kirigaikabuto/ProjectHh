from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from company.models import Vacancy
# Create your views here.


def studentLogin(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 or len(password) == 0:
            error = "Заполните все поля"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main_page")
            else:
                error = "Нет пользователя по такому Username или Password"
    context = {
        "error": error
    }
    return render(request, "students/student_login.html", context)


def profileCreate(request):
    error = ""
    return error


def studentMain(request):
    error=""
    vacancies = None
    if request.method=="POST":
        name = request.POST['name']
        option = request.POST['option']
        if option == "empty" or option == "vacancy":
            vacancies = Vacancy.objects.filter(name__contains=name)
        elif option == "company":
            vacancies = Vacancy.objects.filter(company__name__contains=name)
        elif option == "speciality":
            vacancies = Vacancy.objects.filter(speciality__name__contains=name)
        elif option == "elective":
            vacancies = Vacancy.objects.filter(elective__name__contains=name)
        if len(vacancies)==0:
            error="Нет вакансий"
    else:
        vacancies = Vacancy.objects.all()
    context = {
        "vacancies": vacancies,
        "error":error
    }
    return render(request, "students/room.html",context)


def userLogout(request):
    logout(request)
    return redirect("main_page")


def studentProfile(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        datebirth = request.POST['datebirth']
        speciality = int(request.POST['speciality'])
        elective = int(request.POST['elective'])
        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0:
            error = "Все поля должны быть заполнены"
        else:
            specialityObject = models.Speciality.objects.get(pk=speciality)
            electiveObject = models.Elective.objects.get(pk=elective)
            studentProfile = models.Student()
            if request.user.first_name:
                studentProfile = models.Student.objects.get(user = request.user)
            studentProfile.elective = electiveObject
            studentProfile.speciality = specialityObject
            studentProfile.datebirth = datebirth
            studentProfile.first_name = first_name
            studentProfile.last_name = last_name

            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            studentProfile.user = user
            studentProfile.save()
    specialities = models.Speciality.objects.all()
    elective = models.Elective.objects.all()

    context = {
        "specialities": specialities,
        "elective": elective,
        "error": error,
    }
    if request.user.first_name:
        profile = models.Student.objects.get(user=request.user)
        context ={
            "profile":profile
        }
    return render(request, "students/profile.html", context)
