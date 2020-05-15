from django.shortcuts import render,redirect

# Create your views here.
def pillowsite_index(request):
	return render(request, "pillow_site_html/index.html", {})