from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.wordhome, name = "wordhome"),
    path('about/',views.wordabout, name = "wordabout"),
    path('result/',views.wordresult, name = "wordresult"),
]