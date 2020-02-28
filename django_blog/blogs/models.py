from django.db import models
from django.contrib.auth.models import User #
from django.utils import timezone #
import datetime

# Create your models here.
class Blog(models.Model):
    """記事"""
    
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_date = models.DateField(default=datetime.date.today())
    updated_date = models.DateField(auto_now=True)

    def get_previous_by_pk(self):
        return type(self).objects.filter(pk__lt=self.pk).order_by('pk').last()

    def get_next_by_pk(self):
        return type(self).objects.filter(pk__gt=self.pk).order_by('pk').first()

    def __str__(self):
        return self.title


class Comment(models.Model):#
    """コメント"""

    name = models.CharField(max_length=150, blank=False)
    text = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.name
