from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name='login'),
    path('signUp/', signUp, name='signUp'),
    path('user_verify/', user_verify, name='user_verify'),
]
