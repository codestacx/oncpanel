from django.urls import path,include
from corononalive import scraper
urlpatterns = [
    path('',include('scraper.urls'))
]
