from django.shortcuts import render
from eminer.models import NewEntry
from django.http import HttpResponse
# Create your views here.

def BlogView(request, post_name=None, count=0):
    if post_name == None:
        count = int(count)
        posts = NewEntry.objects.order_by('-posted')[count:count+2]
        count += 2
        """try:
            posts = NewEntry.objects.order_by('-posted')[count:count+5]
            count = count + 5
        except DoesNotExist:
            posts = NewEntry.objects.order_by('-posted')[:5]"""
        val = 0
    else:
        posts = NewEntry.objects.get(slug=post_name)
        val = 1
    return render(request, 'eminer/index.html', {'posts':posts, 'val':val, 'count':count})
def About(request):
    return render(request, 'eminer/about.html')