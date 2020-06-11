
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path("students/",include("university.urls")),
    path("company/",include("company.urls")),
]
