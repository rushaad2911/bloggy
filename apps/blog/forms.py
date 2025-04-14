from django import forms
from .models import BlogModel
from ..user.models import Interest



class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','content','tags']
    tags = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),  # Query all available interests
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for selection
        required=True
    )