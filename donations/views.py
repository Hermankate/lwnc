from django.shortcuts import render
from  paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

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
    inputprice =3
    amount = inputprice# must be picked from either the choice or what the user inputs
    host = request.get_host()
    paypal_donate = {
        'business':settings.PAYPAL_RECIEVER_EMAIL,
        'amount': amount,
        'invoice': uuid.uuid4(),
        'currency_code':'USD',
        'notify_url':f"http://{host}{reverse('paypal-ipn')}",
        'return_url':f"http://{host}{reverse('index')}",#page when donation was successfull
        'cancel_url':f"http://{host}{reverse('donate')}"#page when donation was unsuccessfull

    }
    paypal_donated=PayPalPaymentsForm(initial=paypal_donate)

    context ={
        'paypal':paypal_donated
    }

    return render(request,'donate.html', context )

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

