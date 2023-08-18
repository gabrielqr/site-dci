from django.contrib import admin
from .models import Post, MensagemContato, Carrossel, Projeto, DropdownProjeto

admin.site.register(Post)
admin.site.register(MensagemContato)
admin.site.register(Carrossel)
admin.site.register(Projeto)
admin.site.register(DropdownProjeto)