from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    minidescription = models.CharField(max_length = 1000, default=None, blank=True, null=True)
    maintext = models.TextField(default=None, blank=True, null=True)
    uploadTime = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title