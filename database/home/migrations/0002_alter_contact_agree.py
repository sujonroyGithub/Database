# Generated by Django 4.0.4 on 2022-07-30 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='agree',
            field=models.CharField(max_length=144),
        ),
    ]