# Generated by Django 3.2.19 on 2023-10-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_permisoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='adicionar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dicionar', models.TextField(max_length=20)),
            ],
        ),
    ]