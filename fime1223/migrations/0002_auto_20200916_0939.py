# Generated by Django 3.1.1 on 2020-09-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_consultancy',
            field=models.BooleanField(default=False),
        ),
    ]
