from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Vacancy, ChoiceVacancy
from university.models import Student, StudentSkills


def company_main(request):
    return render(request, "company/main.html")


def register(request):
    return render(request, "company/register.html")


def signup(request):
    return render(request, 'company/register.html')


def singin(request):
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
                return redirect("company_main")
            else:
                error = "Нет пользователя по такому Username или Password"
    context = {
        "error": error
    }
    return render(request, "company/login.html", context)


def company_private(request):
    vacancies = Vacancy.objects.all().filter(company__user=request.user)
    d = {
        "vacancies": vacancies
    }
    return render(request, "company/company_room.html", context=d)


def company_vacancy(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    senders = ChoiceVacancy.objects.all().filter(vacancy=vacancy)
    d = {
        "vacancy": vacancy,
        "senders": senders,
    }
    return render(request, "company/company_vacancy.html", context=d)


def student_detail(request, pk, id):
    student = Student.objects.get(pk=pk)
    vacancy = Vacancy.objects.get(pk=id)
    student_skills = StudentSkills.objects.all().filter(student=student)
    d = {
        "student": student,
        "skills": student_skills,
        "vacancy": vacancy,
    }

    return render(request, "company/student_detail.html", context=d)


def accept_vacancy(request, pk, id):
    student = Student.objects.get(pk=pk)
    vacancy = Vacancy.objects.get(pk=id)
    choiced_vacancy = ChoiceVacancy.objects.get(vacancy=vacancy, student=student)
    choiced_vacancy.success = True
    choiced_vacancy.save()
    return redirect("company_main")
