from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('builder/', views.builder, name='builder'),
    path('preview/', views.preview, name='preview'),
    path('p/<slug:slug>/', views.public_portfolio, name='public_portfolio'),
]
