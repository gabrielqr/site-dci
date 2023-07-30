from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(null=True, blank= True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)