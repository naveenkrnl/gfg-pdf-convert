from django.shortcuts import render, HttpResponse
from .forms import InputForm
import pdfkit 
import requests
from bs4 import BeautifulSoup
import os
from wsgiref.util import FileWrapper

# Create your views here.
def download_view(request):
    context={

    }
    form = InputForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            url = form.cleaned_data.get("URL")
            page=requests.get(url)
            # content = open("shaurya", "r"/)
            # file.write(page.text)
            # file.close()
            # content=file("shaurya.pdf").read()
            pdfkit.from_url(url,'shaurya.pdf') 
            content = open("shaurya.pdf", "rb")

            soup = BeautifulSoup(page.text,'lxml')
            title = soup.find("title").get_text()
            response = HttpResponse(FileWrapper(content), content_type='application/pdf')
            response['Content-Length'] = os.path.getsize("shaurya.pdf")
            response['Content-Disposition'] = 'attachment; filename=%s' % (title+".pdf")
            return response

    context["form"]=form
    return render(request,"main.html",context)