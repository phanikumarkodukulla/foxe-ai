from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ask/', views.ask_gemini, name='ask_gemini'),
]