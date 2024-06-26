# Generated by Django 4.2.6 on 2023-11-04 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_rename_adminmanagebank_bank_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='blood_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_group', models.CharField(max_length=100)),
                ('b_deatils', models.CharField(max_length=100)),
                ('b_expiry', models.CharField(max_length=100)),
                ('b_status', models.CharField(max_length=100)),
                ('bank_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank_reg')),
            ],
        ),
        migrations.DeleteModel(
            name='recipient',
        ),
    ]
