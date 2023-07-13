from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date_view(request):
    if request.method == 'GET':
        current_date = datetime.now().strftime("%d-%m-%Y")
        return HttpResponse(current_date)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
