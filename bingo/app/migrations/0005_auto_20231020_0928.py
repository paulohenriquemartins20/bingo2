# Generated by Django 3.2.19 on 2023-10-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_pisx_permisoes_chavep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisoes',
            name='chavep',
        ),
        migrations.RemoveField(
            model_name='permisoes',
            name='nomeunico',
        ),
        migrations.RemoveField(
            model_name='permisoes',
            name='numeros',
        ),
        migrations.AlterField(
            model_name='permisoes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
