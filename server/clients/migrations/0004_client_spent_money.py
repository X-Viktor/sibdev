# Generated by Django 3.1.4 on 2020-12-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20201210_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='spent_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]