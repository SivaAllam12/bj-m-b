from django.shortcuts import render
from .models import Job
def home(request):
    jobs=Job.objects
    return render(request,'homepage.html',{'jobs':jobs})
