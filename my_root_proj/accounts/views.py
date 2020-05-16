from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .tokens import account_activation_token
from .forms import SignupForm

# Create your views here.
def shop_signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.email = form.cleaned_data.get('email')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/shop/index')
	else:
		form = SignupForm()
	return render(request, "pillow_site_html/signup.html", { 'form':form })

def shop_login(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('/shop/index')
	else:
		form = AuthenticationForm()
	return render(request, "pillow_site_html/login.html", { 'form':form })

def shop_logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/shop/index')
		