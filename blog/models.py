from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    # on_delete=models.CASCADE means that if auther delete, delete all article
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

