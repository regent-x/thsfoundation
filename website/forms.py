from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Investor

class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        widgets = {
            "Date_of_Birth": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            ),
            "Phone": PhoneNumberPrefixWidget(
                initial="NG",
            ),
            "Whatsapp": PhoneNumberPrefixWidget(
                initial="NG",
            ),
            "Ref": forms.NumberInput(
                attrs={"type": 'number',"id": "numberField"}
            ),
        }