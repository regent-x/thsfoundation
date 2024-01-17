from django import forms
<<<<<<< HEAD
from .models import Investor

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
=======

from .models import Investor

class InvestorForm(forms.Form):
    class Meta:
        model = Investor
        fields = '__all__'
>>>>>>> refs/remotes/origin/main
