from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
class FreeCheckOutForm(forms.Form):
    check_out_number = forms.IntegerField(validators=[MinValueValidator(1)])
