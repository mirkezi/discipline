# Generated by Django 4.2.13 on 2024-07-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplineapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
