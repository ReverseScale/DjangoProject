from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # created_time = models.DateTimeField(default = timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return "<Article:%s>" % self.title
