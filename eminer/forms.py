from django import forms
from eminer.models import NewEntry, Tag
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, ButtonHolder

class EntryForm(forms.ModelForm):
    class Meta:
        model=NewEntry
        fields = ('title','body','tag')
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            'first arg is the legend of the field set',
            'title',
            'body',
            'tag',
            css_class = 'post_form'
        ),
        ButtonHolder(
            Submit('submit','Submit',css_class='btn-primery')
        )
    )
    helper.form_method = 'POST'

    
class EditPostForm(forms.ModelForm):
    class Meta:
        model=NewEntry
        fields = ('title','body','tag')
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('edit','Submit', css_class='btn-primery'))
    
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields=('slug',)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Add', css_class='btn-primery'))
    
    
class PublishForm(forms.ModelForm):
    class Meta:
        model = NewEntry
        fields=('published',)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Publish', css_class='btn-primery'))