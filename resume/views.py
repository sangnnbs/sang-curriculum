from django.shortcuts import render
from .models import Profile, Skill

# Create your views here.
def homepage(request):
	return render(request = request, template_name="resume/home.html")

# View for Profile Model
def profile(request):
	profile = Profile.objects.get(pk = 1)
	skill = Skill.objects.get(pk = 1)
	context = {
        'profile': profile,
        'skill' : skill
    }

	return render(request = request, template_name="resume/index.html", context= context)
	
