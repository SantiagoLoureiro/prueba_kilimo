# Generated by Django 3.1.1 on 2020-09-26 15:54

from django.db import migrations, models
import django.db.models.deletion


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
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('quantity', models.FloatField()),
                ('date', models.DateField()),
                ('filed_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rain', to='field.field')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
