from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Vacancy)
admin.site.register(models.CompanyType)
admin.site.register(models.ChoiceVacancy)