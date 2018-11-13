from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blogi(request):
    blogi = Blog.objects
    return render(request, 'blog/blog.html', {'blogi':blogi})

def blogcalosc(request, blog_id):
    calosc = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/calosc.html', {'calosc':calosc})
