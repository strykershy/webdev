from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=300)
    slug = models.SlugField()
    article_text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.article_title

    def snippet(self):
        return self.article_text[:50] + '...'
