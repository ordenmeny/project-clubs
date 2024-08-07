# Generated by Django 4.2.13 on 2024-07-17 12:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collab', '0008_alter_clubmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmodel',
            name='valid_team',
            field=models.ManyToManyField(blank=True, null=True, related_name='valid_team_club_model', to=settings.AUTH_USER_MODEL, verbose_name='Участники клуба'),
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='request_team',
            field=models.ManyToManyField(blank=True, null=True, related_name='request_team_club_model', to=settings.AUTH_USER_MODEL, verbose_name='Заявки на участие'),
        ),
    ]
