# Generated by Django 3.1 on 2020-08-31 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200901_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_mumber',
            field=models.CharField(max_length=10),
        ),
    ]
