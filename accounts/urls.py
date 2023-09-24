""" defines url patterns for accounts"""

from atexit import register
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    #include default auth url
    path('', include('django.contrib.auth.urls')),
    #registration page
    path('register/', views.register, name='register')
]