from django.db import models
from django.contrib.auth.models import User

class Speciality(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Elective(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="student")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    datebirth = models.DateField(blank=True, null=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, blank=True, null=True)
    elective = models.ForeignKey(Elective, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentSkills(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


