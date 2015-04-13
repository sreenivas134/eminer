from django.db import models
from django_markdown.models import MarkdownField 
# Create your models here.

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    
    def __unicode__(self):
        return self.slug

class NewEntry(models.Model):
    title = models.CharField(max_length=200,)
    body = MarkdownField()
    published = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length = 200,)
    tag = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.title