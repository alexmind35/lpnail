from django.shortcuts import render
from logotype.models import Logo
from mainpage.models import About

def mainpage_list(request):
    logotype = Logo.objects.all()
    mainpage = About.objects.all()
    return render(request, "mainpage/mainpage_list.html", {"mainpage": mainpage, "logotype": logotype})