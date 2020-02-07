from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    user = models.CharField(default='Anonymous', max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField()
    date_posted = models.TextField(default=timezone.now)
    # default date | formatted
    # datetime.datetime.now().strftime("%B, %a %d %Y")

    def __str__(self):
        return self.title
