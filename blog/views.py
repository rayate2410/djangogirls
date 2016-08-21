from django.shortcuts import render

# Create your views here.

def blogs_list(request):
	return render(request, 'blogs_list.html', {})