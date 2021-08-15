from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Create your views here.
def home(request):
    url = "https://www.moh.gov.sg/covid-19-phase-advisory"
    news = "https://www.straitstimes.com/coronavirus"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rules = soup.findAll('div', {'class':'activity-container'})

    Text_lst = []
    Text_lst.clear
    context = 0

    for rule in rules[:19]:
        title = rule.find('p').text
        title=title.replace("^^","\n")
        title=title.replace("^^.","\n")
        title=title.replace("^","\n")
        title=title.replace("\n"," ")
        Text_lst.append(title)
    context = {'Text_lst' : Text_lst}
	
    return render(request, 'accounts/dashboard.html', context)