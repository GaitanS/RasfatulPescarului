# Generated by Django 5.1.2 on 2024-11-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_lake_google_map_url_lake_google_map_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lake',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
