from django.urls import path
from django.contrib.auth import views

from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login')
]