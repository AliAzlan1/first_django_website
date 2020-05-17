from django.contrib.sites.shortcuts import get_current_site #activate
from django.contrib.auth.models import User #activate
from django.contrib.auth import login, authenticate, logout #shop_login,shop_logout
from django.utils.encoding import force_bytes,force_text #shop_signup,activate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode #account_activation_sent,activate
from django.template.loader import render_to_string #account_activation_sent
from django.shortcuts import render,redirect #almost all functions
from .tokens import account_activation_token #activate
from .forms import SignupForm #signup

# Create your views here.
def shop_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			#user.refresh_from_db()
			#user.profile.email = form.cleaned_data.get('email')
			user.save()
			#raw_password = form.cleaned_data.get('password1')
			#user = authenticate(username=user.username, password=raw_password)
			#login(request, user)
			#return redirect('/shop/index')
			current_site = get_current_site(request)
			subject = 'Activate Your MySite Account'
			message = render_to_string('pillow_site_html/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)
			return redirect('/shop/account_activation_sent')
	else:
		form = SignupForm()
	return render(request, "pillow_site_html/signup.html", { 'form':form })

def shop_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/shop/index')
		else:
			return render(request, "pillow_site_html/login.html", {})
	else:
		return render(request, "pillow_site_html/login.html", {})

def shop_logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/shop/index')
		
def account_activation_sent(request):
	return render(request, "pillow_site_html/account_activation_sent.html")

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('/shop/index')
	else:
		return render(request, 'account_activation_invalid.html', {})