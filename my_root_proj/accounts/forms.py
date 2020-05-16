from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Email',  'required':'True'}))
	username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Username'}))
	password1 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Enter password'}))
	password2 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

	class Meta():
		model = User
		fields = ('username','email','password1','password2',)