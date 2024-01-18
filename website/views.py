from django.shortcuts import render, redirect
from .forms import InvestorForm

from django.core.mail import send_mail


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
    Subject = 'Registration succesful.'
    msg = f"""Dear {request.session['name']}, welcome to the ths family,
             We are glad to have you among us. 
             To complete the investment process.
             Send your seed money to the account
             below then you message our customer 
             care on whatsapp with your reciept 
             and your ref number {request.session['ref']}. """
    send_mail(Subject, msg, "theholyseed07@gmail.com",[f"{request.session['email']}"])
    return render(request, 'welcome.html')
