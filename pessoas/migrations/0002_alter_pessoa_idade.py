# Generated by Django 4.2 on 2023-05-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(),
        ),
    ]