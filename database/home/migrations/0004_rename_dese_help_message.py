# Generated by Django 4.0.4 on 2022-07-31 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_help'),
    ]

    operations = [
        migrations.RenameField(
            model_name='help',
            old_name='dese',
            new_name='message',
        ),
    ]
