from django.urls import path
from .views import avatar_customization

urlpatterns = [
    path('customize/', avatar_customization, name='avatar'),
]
