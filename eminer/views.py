from django.shortcuts import render
from eminer.models import NewEntry, Tag
from eminer.forms import EntryForm
from django.http import HttpResponse
# Create your views here.

def BlogView(request, post_name=None, count=0, tag=None):
    recent = NewEntry.objects.order_by('-posted')[:5]
    if post_name:
        posts = NewEntry.objects.filter(slug=post_name)
    elif tag:
        tags = Tag.objects.get(slug=tag)
        posts = NewEntry.objects.filter(tag = tags)
    else:
        count = int(count)
        posts = NewEntry.objects.order_by('-posted')[count:count+2]
        count += 2
    return render(request, 'eminer/index.html', {'posts':posts, 'count':count, 'recent':recent})
def About(request):
    return render(request, 'eminer/about.html')

def AddPost(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            form.save_m2m()
            return BlogView(request)
        else:
            print form.errors
            
    else:
        form = EntryForm()
        
    return render(request, 'eminer/add_post.html',{'form':form})