from django.shortcuts import render,redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import Data

def scrape(request):
    if request.method == "POST":
        someting = request.POST.get("site","")   
        page = requests.get(someting)
        soup = BeautifulSoup(page.text, "html.parser")
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Data.objects.create(link=link_address, name=link_text)
            
        return redirect("/")
    else:
        links = Data.objects.all()    
    return render(request, "myapp/show.html", {"links": links})


def clear(request):
    Data.objects.all().delete()
    return render(request,"myapp/show.html")