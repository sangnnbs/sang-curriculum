from django.urls import path
from . import views

app_name = "resume"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile", views.profile, name="profile")
]