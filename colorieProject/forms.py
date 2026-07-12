from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select author")

    class Meta:
        model = Blog
        fields = ["title", "text", "author", "published_date"]
        # widgets = {
        #     "title" : forms.TextInput(attrs={
        #         "class": "text-xl bold text-blue-900",
        #         "placeholder":"Enter blog title"
        #     }),
        #     "author": forms.Select(attrs={
        #         "class": "text-xs semibold rounded-md w-full block"
        #     }),
        #     "published_date": forms.DateInput(attrs={
        #         "type" : "date",
        #         "class": "rounded-md w-full block"
        #     })
        # }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(label="Enter your email")
    message = forms.CharField(widget=forms.Textarea, label="Type your message here")