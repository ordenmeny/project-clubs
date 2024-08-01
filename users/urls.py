from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('api/v1/user-data/<slug:verif_code>/', UserDataAPIViewVerificationCode.as_view(), name='api_user_data'),
]

