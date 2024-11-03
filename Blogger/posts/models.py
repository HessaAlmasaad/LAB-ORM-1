from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at  = models.DateTimeField(default=datetime.now, blank=True)