# Generated by Django 3.1.1 on 2020-09-27 02:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.FloatField()),
                ('date', models.DateField()),
                ('field_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rain', to='field.field')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
