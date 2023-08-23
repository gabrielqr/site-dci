from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class Post(models.Model):
    title = models.CharField(max_length=35)
    resumo = models.CharField(max_length=58)
    body = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField(null=False, blank= False, upload_to='posts/')
    imagem_noticia = models.ImageField(null=False, blank= False, upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    publicar = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome

    
    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)

class Carrossel(models.Model):
    title = models.CharField(max_length=50, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    imagem_carrosel = models.ImageField(null=False, blank=False, upload_to='carrossel/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Projeto(models.Model):
    title = models.CharField(max_length=30, blank=False)
    link = models.URLField(blank=False)
    
    def __str__(self):
        return self.title
    
class DropdownProjeto(models.Model):
    title = models.CharField(max_length=30, blank=False)
    link = models.URLField(blank=False)
    
    def __str__(self):
        return self.title
    
class CardIcone(models.Model):
    title = models.CharField(max_length=50, blank=False)
    link = models.URLField(blank=False)
    icon = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]