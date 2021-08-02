from django import forms

class login_frm(forms.Form):
    user = forms.CharField(max_length= 20, label='usuario')
    passw = forms.CharField(max_length=100, label='password', widget=forms.PasswordInput(attrs={'class':'placeholder'}))