from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class UserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    telegram_chat_id = models.IntegerField(null=True, blank=True)
    telegram_verif_code = models.CharField(null=True, blank=True, max_length=16)
    skills = models.TextField(null=True, blank=True, verbose_name='Навыки')

    class Meta:
        verbose_name_plural = 'Users'

    # def get_absolute_url(self):
    #     return reverse('users:signup', kwargs={'username': self.username})
