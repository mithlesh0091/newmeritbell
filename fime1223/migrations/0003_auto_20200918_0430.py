# Generated by Django 3.1.1 on 2020-09-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0002_auto_20200916_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_informationinfo',
            name='Basic_information_school_logo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
