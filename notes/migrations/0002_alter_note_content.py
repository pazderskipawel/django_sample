# Generated by Django 4.1.3 on 2022-12-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(default='Notatka...'),
        ),
    ]
