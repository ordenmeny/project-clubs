from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget


class ClubModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = ClubModel
        fields = ['name', 'desc', 'tags', 'text', 'required_team']



class SendMsgForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)