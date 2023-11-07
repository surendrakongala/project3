from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('<h1><marquee>hi jampandu how are you</marquee></h1>')