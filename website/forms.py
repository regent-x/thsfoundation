from django import forms

from .models import Investor

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        widgets = {
            "Date_of_Birth": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            )
        }