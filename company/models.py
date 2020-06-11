from django.db import models
from django.contrib.auth.models import User
from university.models import Speciality,Elective
# Create your models here.


class Company(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="company")
    name = models.CharField(max_length=255)
    speciality =  models.ForeignKey(Speciality,on_delete=models.CASCADE,blank=True,null=True,related_name="speciality")
    elective = models.ForeignKey(Elective,on_delete=models.CASCADE,blank=True,null=True,related_name="elective")
    def __str__(self):
        return self.name

class VacancyRequirements(models.Model):
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE)


