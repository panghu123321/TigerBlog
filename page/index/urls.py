from django.urls import path
from page.index.views import index

urlpatterns = [
    path('', index),
]
