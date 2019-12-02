from django.contrib import admin
from django.urls import path
from server.views import Login, Register

app_name = 'server'
urlpatterns = [
    
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='resigter')
]
