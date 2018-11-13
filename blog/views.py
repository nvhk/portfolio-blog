from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogi(request):
    blogi = Blog.objects
    return render(request, 'blog/blog.html', {'blogi':blogi})
