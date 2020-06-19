from django.db import models
from django.contrib.auth.models import User
from university.models import Speciality, Elective,Student


# Create your models here.

class CompanyType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(CompanyType, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="speciality")
    elective = models.ForeignKey(Elective, on_delete=models.CASCADE, blank=True, null=True, related_name="elective")
    description = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class VacancyRequirements(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)


class ChoiceVacancy(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    message = models.TextField(null = True,blank=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.vacancy.name+"<-"+self.student.user.username