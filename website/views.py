from django.shortcuts import render, redirect
from .models import Investor
from .forms import InvestorForm
from django.core.mail import EmailMessage
import os


# Create your views here.
def landing(request):
    return render(request, "landing.html")


def signup(request):
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            request.session['name']= form.cleaned_data['Firstname']
            request.session['email'] = form.cleaned_data['Email']
            form.save()
            return redirect("/welcome")
    else:
        form = InvestorForm()
    return render(request, 'signup.html', { 'form': form})


def welcome(request):
    investor = Investor.objects.get(request.session["name"])
    for base, dir, file in os.walk('.'):
        if file == 'Account_number.jpg':
            with open( file, 'rb') as file:
                 file_content = file.read()
    
            Subject = 'Registration succesful.'

            msg = f"""Dear {request.session.get('name')}
             welcome to the THS Family. We are glad to have you among us.
             To complete the investment process, Send your seed money to the account number in the image attachment sent to you. below then you message our customer service on whatsapp with your reciept 
             and your ref number {investor.Id}"""

            email = EmailMessage(Subject, msg,  "theholyseed07@gmail.com", [f"{request.session.get('email')}"])
            email.attach(file, file_content, "image/png")
            email.send()
            return render(request, 'welcome.html')
        else:
            continue
            HttpResponse()

    
