# Generated by Django 2.0 on 2018-07-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='passw',
            field=models.CharField(max_length=25),
        ),
    ]
