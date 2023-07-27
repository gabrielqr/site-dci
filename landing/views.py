from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def index(request):
#     return render(request, 'index.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    
class DetalhesNoticiasView(DetailView):
    model = Post
    template_name = 'detalhes_noticias.html'