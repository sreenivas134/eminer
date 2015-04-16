from django import forms
from eminer.models import NewEntry, Tag
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EntryForm(forms.ModelForm):
    title = forms.CharField(max_length=200,)
    body = forms.CharField(widget=MarkdownWidget,)
    published = forms.BooleanField(widget=forms.HiddenInput, required=False)
    posted = forms.DateTimeField(widget=forms.HiddenInput, required=False)
    modified = forms.DateTimeField(widget=forms.HiddenInput, required=False)
    slug = forms.SlugField(widget=forms.HiddenInput, required=False)
    tag = forms.SlugField(max_length=200,)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Submit', css_class='btn-primery'))
    
    class Meta:
        model=NewEntry
        fields = ('title','body','tag')
    