from decouple import config
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), {'PROJECT_ID': config("PROJECT_ID")}, name='index'),
]
