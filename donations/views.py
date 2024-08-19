from django.shortcuts import render

# Create your views here.
# index page.
def index(request):
    return render(request,'index.html', {})

# about page.
def about(request):
    return render(request,'about.html', {})

# blog page.
def blog(request):
    return render(request,'blog.html', {})

# causes page.
def causes(request):
    return render(request,'causes.html', {})

# contact page.
def contact(request):
    return render(request,'contact.html', {})

# donate page.
def donate(request):
    return render(request,'donate.html', {})

# event page.
def event(request):
    return render(request,'event.html', {})

# service page.
def service(request):
    return render(request,'service.html', {})

# single page.
def single(request):
    return render(request,'single.html', {})

# team page.
def team(request):
    return render(request,'team.html', {})

# volunteer page.
def volunteer(request):
    return render(request,'volunteer.html', {})

