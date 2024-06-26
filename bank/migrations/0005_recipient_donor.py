# Generated by Django 4.2.6 on 2023-10-30 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_adminmanagebank'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('blod_type', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.login')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('blod_type', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.login')),
            ],
        ),
    ]
