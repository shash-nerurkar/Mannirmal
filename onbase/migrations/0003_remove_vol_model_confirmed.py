# Generated by Django 3.1.5 on 2021-04-30 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onbase', '0002_vol_model_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol_model',
            name='confirmed',
        ),
    ]
