from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model) :
    username = models.CharField(default = 'New user', max_length = 60)
    
    def __str__(self) :
        return f'{self.username} Profile'