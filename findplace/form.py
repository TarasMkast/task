from django import forms


class PlaceForm(forms.Form):
    type_place = forms.CharField(max_length=10, help_text='Enter one type of institution, for example: cafe, police')
    address = forms.CharField(help_text='Enter the inital address, for example: "Івано-Франківськ, Мазепи 42"')
    email = forms.EmailField(help_text='Enter your email please')

