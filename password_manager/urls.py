from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_terminal, name='password_terminal'),
    path('execute-command/', views.password_terminal, name='execute_command'),
]
