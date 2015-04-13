from django.shortcuts import render
from eminer.models import NewEntry
from django.http import HttpResponse
# Create your views here.

def BlogView(request):
    posts = NewEntry.objects.order_by('-posted')[:5]
    if posts:
        return render(request, 'eminer/index.html', {'posts':posts})
    else:
        return render(request, 'eminer/index.html',{'posts':post.errors})

def About(request):
    return render(request, 'eminer/about.html')