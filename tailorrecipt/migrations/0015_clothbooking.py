# Generated by Django 5.0.6 on 2024-10-07 06:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailorrecipt', '0014_remove_user_dob_remove_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='clothbooking',
            fields=[
                ('Booking_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Mail_Id', models.CharField(max_length=100, unique=True)),
                ('Mobile_No', models.IntegerField(max_length=10)),
                ('Upper_Wear', models.TextField()),
                ('Lower_Wear', models.TextField()),
                ('Description', models.TextField()),
                ('quantity', models.IntegerField(max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='date published')),
                ('Status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
    ]
