from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Article(models.Model) :
    author  = models.ForeignKey(User, on_delete = models.CASCADE)
    title   = models.CharField(max_length = 60 )
    content = models.TextField()
    date_posted     = models.TextField(default = datetime.datetime.now().strftime("%B, %a %d %Y"))

    def __str__(self):
        return self.title