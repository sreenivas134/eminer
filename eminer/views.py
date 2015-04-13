from django.shortcuts import render
from eminer.models import NewEntry
# Create your views here.

"""class BlogView(request):
    posts = NewEntry.objects.order_by('-posted')[:5]
    return render(request, 'emine/blog.html',{'posts':posts})"""