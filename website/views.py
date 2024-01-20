from django.shortcuts import render, redirect
from .forms import InvestorForm

import magic
import os

from django.core.mail import EmailMessage


# Create your views here.
def landing(request):
    return render(request, "landing.html")


def signup(request):
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            request.session['name']= form.cleaned_data['Firstname']
            request.session['ref'] = form.cleaned_data['Ref']
            request.session['email'] = form.cleaned_data['Email']
            form.save()
            return redirect("/welcome")
    else:
        form = InvestorForm()
    return render(request, 'signup.html', { 'form': form})


def welcome(request):
    path_to_file = "../Account_number.jpg"

    with open( path_to_file , 'rb') as file:
        file_content = file.read()
    
    mime_type = magic.from_buffer(file_content, mime=True)

    Subject = 'Registration succesful.'

    email = EmailMessage(Subject, msg,  "theholyseed07@gmail.com", [f"{request.session['email']}"])
    email.attach(path_to_file, file_content, mime_type)
    msg = f"""Dear {request.session['name']}, welcome to the THS Family,
     We are glad to have you among us. To complete the investment process, Send your seed money to the account
     below then you message our customer serviceon whatsapp with your reciept 
     and your ref number {request.session['ref']}. """

    return render(request, 'welcome.html')
