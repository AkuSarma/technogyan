from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(TemplateView):
    template_name = "registration/profile.html"