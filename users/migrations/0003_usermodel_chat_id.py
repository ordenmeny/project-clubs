# Generated by Django 4.2.13 on 2024-07-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='chat_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]