# Generated by Django 2.1.2 on 2019-04-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0006_auto_20190412_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='rollno',
            field=models.CharField(default='', max_length=200),
        ),
    ]
