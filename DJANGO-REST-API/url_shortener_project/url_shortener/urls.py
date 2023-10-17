from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),
    path('user_urls/', views.user_urls, name='user_urls'),
]
