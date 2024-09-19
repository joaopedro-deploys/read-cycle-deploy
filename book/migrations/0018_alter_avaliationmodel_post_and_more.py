# Generated by Django 5.0.6 on 2024-08-03 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_avaliationmodel_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliationmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliations', to='book.bookmodel', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='avaliationmodel',
            name='user',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='user_avaliations', to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
    ]
