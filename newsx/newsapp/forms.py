from django import forms
from . import models

class AddArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['article_title', 'slug', 'article_text', 'thumb' ]
        