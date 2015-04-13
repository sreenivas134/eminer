from django.shortcuts import render
from eminer.models import NewEntry
from django.http import HttpResponse
# Create your views here.

def BlogView(request):
    posts = NewEntry.objects.all
    return render(request, 'eminer/index.html',{'posts':posts})
    
def register(request):
    HttpResponse('Hi How are you')