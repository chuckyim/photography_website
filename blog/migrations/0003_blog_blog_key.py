# Generated by Django 2.2.2 on 2020-12-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201125_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_key',
            field=models.IntegerField(default=999),
        ),
    ]