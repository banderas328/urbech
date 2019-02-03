from django.shortcuts import render
from .models import FrontPage

def home(requset):
    frontPage = FrontPage.objects.filter(title="frontpage")

