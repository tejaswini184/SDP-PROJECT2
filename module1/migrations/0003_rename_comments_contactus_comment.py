# Generated by Django 5.0 on 2024-02-09 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='comments',
            new_name='comment',
        ),
    ]
