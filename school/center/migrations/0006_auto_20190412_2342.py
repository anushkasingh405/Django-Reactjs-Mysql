# Generated by Django 2.1.2 on 2019-04-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_auto_20190411_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='rollno',
            field=models.IntegerField(default=0),
        ),
    ]
