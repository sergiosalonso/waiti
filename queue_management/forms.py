from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class CheckOutNumberForm(forms.Form):
    check_out_number = forms.IntegerField(validators=[MinValueValidator(1)], label="Check out number")
class FreeCheckOutForm(forms.Form):
    pass
