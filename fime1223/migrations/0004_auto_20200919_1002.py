# Generated by Django 3.1.1 on 2020-09-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0003_auto_20200918_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_informationinfo',
            name='Basic_information_school_cover_img',
            field=models.ImageField(upload_to='school_cover/'),
        ),
    ]
