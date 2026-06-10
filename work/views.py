from django.shortcuts import render
from .models import Project, Skill, Experience


def projects(request):
    return render(request, "projects.html", {
        "projects": Project.objects.all(),
    })
