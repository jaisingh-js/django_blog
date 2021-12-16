from .models import Comments
from django.db import models
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'comment']