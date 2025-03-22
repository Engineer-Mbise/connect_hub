from django.forms import ModelForm
from django import forms
from .models import Module,Discussion
from django.contrib.auth.forms import UserChangeForm

class ModuleForm(ModelForm):
    class Meta:
        model=Module
        fields=("name","description",)
        
class DiscussionForm(ModelForm):
    class Meta:
        model=Discussion
        fields=("title",)