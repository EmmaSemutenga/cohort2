from django.shortcuts import render
from .models import Article

# Create your views here.
# Model View Template framework 



def home_page(request):
    articles = Article.objects.all()
    return render(request, 'blog/homepage.html', {'stories':articles})