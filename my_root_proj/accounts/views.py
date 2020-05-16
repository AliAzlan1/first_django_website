from django.shortcuts import render

# Create your views here.
def signup(request):
	return render(request, "pillow_site_html/signup.html", {})

def login(request):
	return render(request, "pillow_site_html/login.html", {})
