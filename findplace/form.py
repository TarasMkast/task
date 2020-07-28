from django import forms
from .models import Objtype


class PlaceForm(forms.Form):
    type_place = forms.ModelChoiceField(queryset=Objtype.objects.all())
    address = forms.CharField(help_text='Enter the inital address, for example: "Івано-Франківськ, Мазепи 42"')
    email = forms.EmailField(help_text='Enter your email please')

