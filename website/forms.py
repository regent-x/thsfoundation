from django import forms

from .models import Investor

class InvestorForm(forms.Form):
    class Meta:
        model = Investor
        fields = '__all__'