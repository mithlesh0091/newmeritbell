# Generated by Django 3.1.1 on 2020-09-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0004_auto_20200919_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_informationinfo',
            name='Basic_information_school_cover_img',
            field=models.FileField(upload_to='school_pdf/'),
        ),
    ]
