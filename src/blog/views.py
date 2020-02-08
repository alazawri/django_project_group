from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
  # return HttpResponse('Homepage')
  return render(request, 'homepage.html')

def about(request):
  # return HttpResponse('About Page')
  return render(request, 'about.html')
