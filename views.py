import requests
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import os

def index(request):
    context = {
        "page_title": "homepage",
        "first_name": "Mickle",
        "last_name": "Nguyen",

    }
    return render(request, "index.html", context)



def resume(request):
    context = {
        "page_title": "resume",
    }
    return render(request, "resume.html", context)


def about(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        "page_title": "about",
    }
    return render(request, "about.html", context)



def github(request):
    response = requests.get('https://api.github.com/users/micklenguyen/repos')
    repos = response.json()
    context = {
        "page_title": "GitHub",
        'github_repos': repos,
    }
    return render(request, "github.html", context)



def blog(request):
    context = {
        "page_title": "blog",
    }
    return render(request, "blog.html", context)







