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


def about(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    content_html = open("content/about.html").read()
    context = {
        "content": content_html,
        "page_title": "about",
    }
    return render(request, "base.html", context)

def resume(request):
    content_html = open("content/resume.html").read()
    context = {
        "content": content_html,
        "page_title": "resume",
    }
    return render(request, "base.html", context)

def blog(request):
    content_html = open("content/blog.html").read()
    context = {
        "content": content_html,
        "page_title": "blog",
    }
    return render(request, "base.html", context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/micklenguyen/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)



