# Generated by Django 3.1.1 on 2020-09-26 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rain',
            old_name='filed_owner',
            new_name='field_owner',
        ),
    ]