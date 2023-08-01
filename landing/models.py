from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    resumo = models.CharField(max_length=500)
    body = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField(null=False, blank= False, upload_to='images/')
    imagem_noticia = models.ImageField(null=False, blank= False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    publicar = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)
