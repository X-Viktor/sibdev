# Generated by Django 3.1.4 on 2020-12-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_deals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deals',
            new_name='Deal',
        ),
    ]
