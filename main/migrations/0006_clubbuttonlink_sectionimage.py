# Generated by Django 5.1.2 on 2025-01-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubButtonLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(default='Alăturați-vă clubului', help_text='Text displayed on the button.', max_length=100)),
                ('button_link', models.URLField(help_text='URL where the button redirects.')),
            ],
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(help_text='Name of the section where the image is used.', max_length=100)),
                ('image', models.ImageField(help_text='Upload the image for this section.', upload_to='section_images/')),
            ],
        ),
    ]
