from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=300)
    slug = models.SlugField()
    article_text = models.TextField()
    author = models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.article_title

class Category(models.Model):
    articles = models.ManyToManyField(Article)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
