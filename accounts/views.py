from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, CustomLogInForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomLoginView(LoginView):
    authentication_form = CustomLogInForm

