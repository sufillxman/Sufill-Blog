from django.urls import path
from .views_api import *

urlpatterns = [
    path('login_api/', loginview.as_view(), name='login_api'),
    path('register_api/', RegisterView.as_view(), name='register_api'),
]