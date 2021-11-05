# Generated by Django 3.2.9 on 2021-11-05 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
        ('companies', '0005_employee_contract_type'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.restaurant')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.company')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='CardTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.card')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
            ],
        ),
    ]