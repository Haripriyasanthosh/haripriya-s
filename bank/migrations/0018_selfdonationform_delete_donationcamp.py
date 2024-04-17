# Generated by Django 4.2.6 on 2024-02-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0017_donationcamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfDonationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5)),
                ('willing_to_donate', models.BooleanField()),
                ('date_of_donation', models.DateField()),
                ('last_donated_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='DonationCamp',
        ),
    ]