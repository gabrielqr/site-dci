from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from theme_pixel.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Post, MensagemContato
import smtplib


#imports para pagination
from django.core.paginator import Paginator

def todas_noticias(request):
  lista_noticias = Post.objects.all()
  
  #setup Pagination
  noticias_por_pagina = 6
  p = Paginator(Post.objects.all().order_by('-created_at'), noticias_por_pagina)
  page = request.GET.get('page')
  qtd_paginas = p.get_page(page)
  
  return render(request, 'pages/todas_noticias.html', 
                {'lista_noticias' : lista_noticias,
                 'qtd_paginas' : qtd_paginas})

def abouts_us(request):
  return render(request, 'pages/about.html')

def contact_us(request):
  if request.method == 'POST':
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
   
    mensagem_contato = MensagemContato(nome=name, email=email, assunto=subject, mensagem=message)
    mensagem_contato.save()
    
  return render(request, 'pages/contact.html')

def landing_freelancer(request):
  return render(request, 'pages/landing-freelancer.html')

def handler404(request, exception):
  return render(request, '404.html')

def blank_page(request):
  return render(request, 'pages/blank.html')


# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = UserLoginForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm


# Components
def accordion(request):
  return render(request, 'components/accordions.html')

def alerts(request):
  return render(request, 'components/alerts.html')

def badges(request):
  return render(request, 'components/badges.html')

def bootstrap_carousels(request):
  return render(request, 'components/bootstrap-carousels.html')

def breadcrumbs(request):
  return render(request, 'components/breadcrumbs.html')

def buttons(request):
  return render(request, 'components/buttons.html')

def cards(request):
  return render(request, 'components/cards.html')

def dropdowns(request):
  return render(request, 'components/dropdowns.html')

def forms(request):
  return render(request, 'components/forms.html')

def modals(request):
  return render(request, 'components/modals.html')

def navs(request):
  return render(request, 'components/navs.html')

def pagination(request):
  return render(request, 'components/pagination.html')

def popovers(request):
  return render(request, 'components/popovers.html')

def progress_bars(request):
  return render(request, 'components/progress-bars.html')

def tables(request):
  return render(request, 'components/tables.html')

def tabs(request):
  return render(request, 'components/tabs.html')

def toasts(request):
  return render(request, 'components/toasts.html')

def tooltips(request):
  return render(request, 'components/tooltips.html')

def typography(request):
  return render(request, 'components/typography.html')

# def index(request):
#     return render(request, 'index.html', {})

class HomeView(ListView):
  model = Post
  ordering = ['-created_at']
  template_name = 'pages/teste.html'
  
  def get_context_data(self, **kwargs):
    noticias = Post.objects.all().order_by('-created_at')
    context = super().get_context_data(**kwargs)
    context['max_posts_to_show'] = 4
    return context
  
    
class DetalhesNoticiasView(DetailView):
  model = Post
  template_name = 'pages/detalhes_noticias.html'