# Generated by Django 3.1 on 2020-08-31 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200901_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_mumber',
            field=models.CharField(max_length=100),
        ),
    ]
