# Generated by Django 3.2.7 on 2021-09-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_auto_20210915_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(default=3),
        ),
    ]