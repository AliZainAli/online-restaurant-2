# Generated by Django 2.0.4 on 2018-04-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
