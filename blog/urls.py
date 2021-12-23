from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"   


urlpatterns = [
    path("", views.blog.as_view(), name="blog-posts"),
    path("create", views.create_view, name="blog-create"),
    path('<id>', views.detail_view, name="blog-detail")
] 

