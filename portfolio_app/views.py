from django.shortcuts import render
from .data import *


def home(request):
    content = {
        "personal_details": personal_details,
        "experience": experience,
        "education": education,
        "about_me": about_me,
        "skills": skills,
        "projects": projects,
    }
    return render(request,'home.html',content)