from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Elective)
admin.site.register(models.Speciality)
admin.site.register(models.StudentSkills)
admin.site.register(models.Skill)
