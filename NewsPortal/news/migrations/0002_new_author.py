# Generated by Django 3.2.9 on 2021-11-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='author',
            field=models.CharField(default='Default value', max_length=64, unique=True),
        ),
    ]
