# Generated by Django 2.2.6 on 2020-01-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191224_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
