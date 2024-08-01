from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'email', 'telegram_chat_id', 'telegram_verif_code']
        model = get_user_model()