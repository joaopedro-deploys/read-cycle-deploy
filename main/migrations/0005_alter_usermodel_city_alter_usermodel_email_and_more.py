# Generated by Django 5.0.6 on 2024-07-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_usermodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='neighborhood',
            field=models.CharField(max_length=100, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='number',
            field=models.CharField(max_length=20, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='state',
            field=models.CharField(max_length=100, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=50, verbose_name='User name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name='CEP'),
        ),
    ]
