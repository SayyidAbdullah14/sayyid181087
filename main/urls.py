from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('D2B/', views.D2B, name='D2B'),
    path('D2H/', views.D2H, name='D2H'),
    path('B2D/', views.B2D, name='B2D'),
    path('B2H/', views.B2H, name='B2H'),
    path('H2D/', views.H2D, name='H2D'),
    path('H2B/', views.H2B, name='H2B'),
]