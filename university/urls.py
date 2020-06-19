
from django.urls import path
from . import views
urlpatterns = [
   path("login/",views.studentLogin,name="studentLogin"),
   path("private/",views.studentMain,name="studentPrivate"),
   path("logout/",views.userLogout,name="userLogout"),
   path("private/profile/",views.studentProfile,name="studentProfile"),
   path("private/profile/skill_form",views.skill_form,name="profileSkillForm"),
   path("private/companies_list/",views.company_list,name="companyList"),
   path("private/company_detail/<int:pk>",views.company_detail,name="companyDetail"),
   path("private/vacancy_detail/<int:pk>",views.vacancy_detail,name="vacancyDetail"),
   path("private/choice_vacancy/<int:pk>",views.choice_vacancy,name="choiceVacancy"),
   path("private/vacancies_choiced/",views.vacancies_choiced,name="vacanciesChoiced"),
   path("private/vacancies_success",views.vacancies_success,name="vacanciesSuccess")
]
