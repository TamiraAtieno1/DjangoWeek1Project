# Generated by Django 4.2.5 on 2023-09-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog2_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog2',
            name='book_title',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
