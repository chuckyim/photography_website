# Generated by Django 2.2.2 on 2020-12-14 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_blog_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('blog', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]