from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    