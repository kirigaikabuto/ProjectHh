from django.shortcuts import render
from company.models import  Vacancy

# Create your views here.

def index(request):
    vacancies = Vacancy.objects.all()
    context={
        "vacancies":vacancies
    }
    return render(request, "main/index.html",context)
