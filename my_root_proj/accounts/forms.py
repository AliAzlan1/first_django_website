from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Email',  'required':'True', 'class': 'form-control'}))
	username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Username', 'class': 'form-control'}))
	password1 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Enter password', 'class': 'form-control'}))
	password2 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Confirm password', 'class': 'form-control'}))

	class Meta():
		model = User
		fields = ('username','email','password1','password2',)