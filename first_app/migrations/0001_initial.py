# Generated by Django 5.0 on 2024-01-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelForms',
            fields=[
                ('name', models.CharField(default='Rohim', max_length=30)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.FloatField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('Agree', models.BooleanField(blank=True)),
            ],
        ),
    ]