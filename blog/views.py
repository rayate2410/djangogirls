from django.shortcuts import render
from .models import Blog
from django.utils import timezone

# Create your views here.

def blogs_list(request):
	blogs = Blog.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'blogs_list.html', {'blogs': blogs})