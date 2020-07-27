from django import forms
from findplace.models import objtypes


class PlaceForm(forms.Form):
    type_place = forms.ChoiceField(choices=objtypes)
    address = forms.CharField(help_text='Enter the inital address, for example: "Івано-Франківськ, Мазепи 42"')
    email = forms.EmailField(help_text='Enter your email please')

