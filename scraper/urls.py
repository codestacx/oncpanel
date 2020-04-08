from django.urls import path
from . import views

urlpatterns = [
    path('',views.results,name='index'),
    path('getresults',views.job,name='getresults'),
    path('results',views.index,name='results')
]