from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import requests
import csv
import shutil
from django.http import HttpResponse
import json
from requests_html import HTMLSession
session = HTMLSession()
import string
import random
def index(request):
    return render(request, 'index.html')
# Create your views here.

def dojob():
    url = "https://www.worldometers.info/coronavirus/";
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html5lib')

    table = soup.select_one('#main_table_countries_today')

    tbody = table.find_next('tbody')

    rows = tbody.find_all('tr')

    data = []
    i = 0
    for row in rows:
        information = {}
        cells = row.find_all('td')
        information['country'] = cells[0].get_text()
        information['total_cases'] = cells[1].get_text()
        information['new_cases'] = cells[2].get_text()
        information['total_death'] = cells[3].get_text()
        information['new_deaths'] = cells[4].get_text()
        information['total_recovered'] = cells[5].get_text()
        information['active_cases'] = cells[6].get_text()
        information['serious_critcial'] = cells[7].get_text()
        information['tot_cases'] = cells[8].get_text()
        information['deaths'] = cells[9].get_text()
        information['total_tests'] = cells[10].get_text()
        information['tests'] = cells[11].get_text()
        data.append(information)
    return data
def job(request):
    obj ={
        'code':random.randrange(100000,999999,5)
    }
    data = dojob()



    return HttpResponse(json.dumps(data), content_type="application/json", status=200)


def results(request):
    return render(request,'results.html')

