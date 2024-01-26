from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Investor
from .forms import InvestorForm
from django.core.mail import EmailMessage
import os
from .email import send_email_with_attachment, send_email_attachment


# Create your views here.
def landing(request):
    return render(request, "landing.html")


def signup(request):
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            request.session['name']= form.cleaned_data['Firstname']
            request.session['email'] = form.cleaned_data['Email']
            request.session['ref'] = form.cleaned_data['Ref']
            form.save()
            return redirect("/welcome")
    else:
        form = InvestorForm()
    return render(request, 'signup.html', { 'form': form})


def welcome(request):
    path = os.getcwd() 
    file = os.path.join(path, 'static/Account_number.jpg')
    Subject = 'Registration succesful.'
    msg = f"""<h1> Dear {request.session.get('name')}</h1>

<p>Glad you are among the few that made it this far.</p>
<p>To complete the investment process, follow the steps below:</p>

<h2>Steps: </h2>
<ol>
  <li> Send your seed money(7k) to the account number in the image below.</li>
  <li> Send a whatsapp text with the following infomation to our customer service https://wa.me/message/KA5EWBJNZD3QN1</li>
    <ol>
      <li>Your REF number:{request.session['ref']}</li>
      <li>The number of seed(s) paid for</li>
      <li>Receipt of payment</li>
    </ol>
  <li>Wait for confirmation.</li>
</ol>

<p>Once confirmed. You'll be added to the official list of investors</p>

<p>We can't wait to make your money work for you.</p>

<p>THSfoundation team.</p>"""
    
    email = request.session['email']
    # send_email_with_attachment(email, Subject, msg, file)
    send_email_attachment(email, Subject, msg, file)

    return render(request, 'welcome.html')
