from django.db import models
from django_markdown.models import MarkdownField 
# Create your models here.

class NewEntry(models.Model):
    title = models.CharField(max_length=200,)
    body = MarkdownField()
    published = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length = 200,)
    
    def __unicode__(self):
        return self.title