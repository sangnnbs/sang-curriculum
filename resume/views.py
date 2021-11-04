from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request = request, template_name="resume/home.html")

def profile(request):
	return render(request = request, template_name="resume/index.html")