from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('getresults',views.job,name='getresults'),
    path('results',views.results,name='results')
]