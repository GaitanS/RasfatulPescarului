# Generated by Django 5.1.2 on 2024-11-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lake',
            name='google_map_url',
        ),
        migrations.AddField(
            model_name='lake',
            name='google_map_iframe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
