# Generated by Django 3.1.1 on 2020-09-27 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0002_auto_20200926_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hectare',
            old_name='filed',
            new_name='field_owner',
        ),
    ]
