from django.contrib import admin
from eminer import models
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

class NewEntryAdmin(MarkdownModelAdmin):
    prepopulated_fields={"slug":("title",),}
    list_view = ('title','posted')

admin.site.register(models.NewEntry, NewEntryAdmin)