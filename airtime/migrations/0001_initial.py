# Generated by Django 4.2.1 on 2023-05-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airtime_number', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=12)),
                ('amount', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
