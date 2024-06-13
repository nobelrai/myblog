from django.shortcuts import render
from .models import Index,  Experience, Education, Skills, Interest, Awards
# Create your views here.
                  

def index(request):
    context = {
        "indexs" : Index.objects.all(),
    }
    return render(request, "index.html", context)

def education(request):
    context = {
        "educations" : Education.objects.all(),
    }
    return render(request, "education.html", context)

def skills(request):
    context = {
        "skills" : Skills.objects.all(),
    }
    return render(request, "skills.html", context)

def interests(request):
    context = {
        "interests" : Interest.objects.all(),
    }
    return render(request, "interests.html", context)

def awards(request):
    context = {
        "awards" : Awards.objects.all(),
    }
    return render(request, "awards.html", context)

def experience(request):
    context = {
        "experiences" : Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def base(request):
     return render(request, template_name="experience.html")