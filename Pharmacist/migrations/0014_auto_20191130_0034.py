# Generated by Django 2.2.6 on 2019-11-29 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0013_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliveryDate',
            field=models.DateField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='confirmationState',
            field=models.CharField(max_length=20),
        ),
    ]
