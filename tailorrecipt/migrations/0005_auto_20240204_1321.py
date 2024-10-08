# Generated by Django 3.2.23 on 2024-02-04 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tailorrecipt', '0004_lowerdetsils_paymentdetails_upperdetsils'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowerdetsils',
            name='Custumerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tailorrecipt.addcustumer'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='Custumerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tailorrecipt.addcustumer'),
        ),
        migrations.AlterField(
            model_name='upperdetsils',
            name='Custumerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tailorrecipt.addcustumer'),
        ),
    ]
