# Generated by Django 3.1.1 on 2020-10-03 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0010_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_informationinfo',
            name='detailse',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='fime1223.customer'),
        ),
        migrations.AlterField(
            model_name='basic_informationinfo',
            name='Basic_information_school_cover_img',
            field=models.ImageField(upload_to=' school_cover/'),
        ),
    ]
