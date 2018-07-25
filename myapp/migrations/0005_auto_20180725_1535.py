# Generated by Django 2.0 on 2018-07-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180725_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passw', models.CharField(max_length=20)),
                ('usern', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100, null=True, unique=True)),
                ('text', models.TextField(max_length=2000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='resume',
        ),
    ]
