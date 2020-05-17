from django.urls import path
from .views import *


urlpatterns = [
    path('webpush/', save_token.as_view(), name='webpush'),
]
