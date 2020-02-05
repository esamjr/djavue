from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model) :
    article_author  = models.ForeignKey(User, on_delete = models.CASCADE)
    article_title   = models.CharField(max_length = 30 )
    article_content = models.TextField()
    date_posted     = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.article_title
    