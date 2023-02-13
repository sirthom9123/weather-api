# Generated by Django 2.2.28 on 2023-02-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForecastData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=355)),
                ('temperature', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=25)),
                ('wind', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Forecast Data',
                'ordering': ('created_date',),
            },
        ),
    ]