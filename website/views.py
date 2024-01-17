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
            form.save()
            return redirect("/welcome")
    else:
        form = InvestorForm()
    return render(request, 'signup.html', { 'form': form})


def welcome(request):
    Subject = 'TestRun'
    msg = "how ya doin'"
    send_mail(Subject, msg, "theholyseed07@gmail.com",['spiritofdamola@gmail.com','bodyofdamola@gmail.com'])
    return render(request, 'welcome.html')
