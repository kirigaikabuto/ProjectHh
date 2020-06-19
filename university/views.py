from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from company.models import Vacancy, Company, ChoiceVacancy


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
    error = ""
    vacancies = None
    if request.method == "POST":
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
        if len(vacancies) == 0:
            error = "Нет вакансий"
    else:
        vacancies = Vacancy.objects.all()
    context = {
        "vacancies": vacancies,
        "error": error
    }
    return render(request, "students/room.html", context)


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
                studentProfile = models.Student.objects.get(user=request.user)
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
        skills = models.StudentSkills.objects.filter(student__user=request.user)
        context = {
            "profile": profile,
            "skills": skills
        }
    return render(request, "students/profile.html", context)


def skill_form(request):
    error = ""
    if request.method == "POST":
        skill_name = request.POST['skill_name']
        skill_select = request.POST['skill_select']
        if len(skill_name) == 0 and len(skill_select) == 0:
            error = "Нужно написать новое название или выбрать из существующих"
        if len(skill_name) != 0 and len(skill_select) != 0:
            error = "Нужно либо написать новое название либо выбрать существующе"
        else:
            new_skill_name = ""
            skill = None
            if len(skill_name) != 0:
                skills = models.Skill.objects.filter(name=skill_name)
                if len(skills) != 0:
                    error = "Такой навык уже существует выберите его"
                new_skill_name = skill_name
                skill = models.Skill(name=new_skill_name)
                skill.save()
            elif len(skill_select) != 0:
                new_skill_name = skill_select
                skill = models.Skill.objects.get(name=new_skill_name)
            if error == "":
                skill_connect = models.StudentSkills(skill=skill, student=models.Student.objects.get(user=request.user))
                skill_connect.save()
                return redirect("studentProfile")
    skills_choiced = models.StudentSkills.objects.filter(student__user=request.user)
    all_skills = models.Skill.objects.all()
    needed_skills = []
    for i in all_skills:
        is_exist = False
        for j in skills_choiced:
            if i.name == j.skill.name:
                is_exist = True
                break
        if not is_exist:
            needed_skills.append(i)

    context = {
        "error": error,
        "skills": needed_skills
    }
    return render(request, "students/skill_form.html", context=context)


def company_list(request):
    companies = Company.objects.all()
    all_info = []
    for i in companies:
        vacancies = Vacancy.objects.filter(company=i)
        all_info.append({
            "company": i,
            "vacancy_count": len(vacancies)
        })
    context = {
        "companies": all_info
    }
    return render(request, "students/company_list.html", context=context)


def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    vacancies = Vacancy.objects.filter(company=company)
    context = {
        "company": company,
        "vacancies": vacancies
    }
    return render(request, "students/company_detail.html", context=context)


def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    student = models.Student.objects.get(user=request.user)

    choice_was=False
    choice = ChoiceVacancy.objects.filter(student=student,vacancy=vacancy)
    print(choice)
    if len(choice)!=0:
        choice_was = True
    context = {
        "vacancy": vacancy,
        "choice":choice_was
    }
    return render(request, "students/vacancy_detail.html", context=context)


def choice_vacancy(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    student = models.Student.objects.get(user=request.user)
    action = ChoiceVacancy(vacancy=vacancy, student=student)
    action.save()
    return redirect("studentProfile")


def vacancies_choiced(request):
    vacancies = ChoiceVacancy.objects.filter(student__user=request.user)
    context={
        "vacancies":vacancies
    }
    return render(request,"students/vacancies_choiced.html",context=context)


def vacancies_success(request):
    vacancies = ChoiceVacancy.objects.filter(success=True)
    context = {
        "vacancies": vacancies
    }
    return render(request, "students/vacancies_success.html", context=context)