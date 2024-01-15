from django.shortcuts import render, redirect
from .forms import InvestorForm

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def signup(request):
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save
            redirect("/welcome")
    else:
        form = InvestorForm()
    return render(request, 'signup.html', { 'form': form})


def welcome(request):
    pass
