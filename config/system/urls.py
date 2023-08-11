from django.urls import path
from config.system.views import install

urlpatterns = [
    path('install/', install, name='install'),
]
