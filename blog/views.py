from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from .forms import PostsForm
# Create your views here.

# Use ListView for Class-Based View
class blog(ListView):
    template_name = "index.html"
    model = Post
    context_object_name = 'posts'

def create_view(request):
    context = {}
    
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,"create_view.html",context)
    
def detail_view(request, id):
     context = {}
     
     context["form"] = Post.objects.get(id = id)
     
     return render(request,"detail_view.html",context)
        
    
# Old view 
#def blog(request):
#    data = Post.objects.all()
#    return render(request,"index.html", {"posts":data})