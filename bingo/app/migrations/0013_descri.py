# Generated by Django 3.2.19 on 2023-10-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_naorepeti'),
    ]

    operations = [
        migrations.CreateModel(
            name='descri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escrevadescricao', models.TextField(max_length=20)),
            ],
        ),
    ]
