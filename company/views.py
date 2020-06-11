from django.shortcuts import render

# Create your views here.
def company_main(request):
    return render(request,"company/main.html")

