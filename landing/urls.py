from django.urls import path
from . import views
from .views import HomeView, DetalhesNoticiasView

urlpatterns = [
#    path('', views.index, name='index'),
    path('', HomeView.as_view(), name="index"),
    path('noticias/<int:pk>', DetalhesNoticiasView.as_view(), name="detalhes_noticias")
]