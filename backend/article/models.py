from django.db import models
from django.utils.text import slugify
import datetime

class Article(models.Model):
    slug        = models.SlugField(blank=True, editable=False)
    user        = models.CharField(default='Anonymous', max_length=60)
    title       = models.CharField(max_length=60)
    content     = models.TextField()
    date_posted = models.DateField(default=datetime.date.today, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return self.title
