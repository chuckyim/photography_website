# Generated by Django 2.2.2 on 2020-12-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='blog_key',
            field=models.IntegerField(default=999),
        ),
    ]