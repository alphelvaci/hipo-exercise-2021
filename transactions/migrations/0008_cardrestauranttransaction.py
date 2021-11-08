# Generated by Django 3.2.9 on 2021-11-08 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_employee_contract_type'),
        ('restaurants', '0001_initial'),
        ('transactions', '0007_companycardtransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardRestaurantTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.card')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.restaurant')),
            ],
        ),
    ]
