# Generated by Django 5.0.4 on 2024-04-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0020_bloodproduct_donorregistration_bloodbank'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('allergens', models.CharField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]