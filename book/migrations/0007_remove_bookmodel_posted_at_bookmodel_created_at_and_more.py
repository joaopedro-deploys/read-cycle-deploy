# Generated by Django 5.0.6 on 2024-07-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_bookmodel_authors_alter_bookmodel_language_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='posted_at',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='created_at',
            field=models.DateField(default='2024-07-01', editable=False),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='descricao'),
        ),
    ]
