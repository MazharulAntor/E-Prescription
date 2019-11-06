# Generated by Django 2.2.6 on 2019-11-04 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('licence', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineForm',
            fields=[
                ('medicineFormId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineFormName', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('medicineTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineTypeName', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineName', models.CharField(max_length=25)),
                ('singleUnitQuantity', models.CharField(max_length=50)),
                ('companyId', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='Company.Company')),
                ('formId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.MedicineForm')),
                ('typeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.MedicineType')),
            ],
        ),
    ]
