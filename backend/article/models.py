from django.db import models
from django.utils.timezone import now
import datetime


class Article(models.Model):
    user = models.CharField(default='Anonymous', max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
