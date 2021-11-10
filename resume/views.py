from django.shortcuts import render
from .models import Profile

# Create your views here.
def homepage(request):
	return render(request = request, template_name="resume/home.html")

def profile(request):
	profile = Profile.objects.get(pk = 1)

	context = {
        'profile': profile,
    }

	return render(request = request, template_name="resume/index.html", context=context)