# Generated by Django 3.2.9 on 2021-11-05 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_cardtransaction_companytransaction_restauranttransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardTopup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_transactions', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='transactions.cardtransaction')),
                ('company_transaction', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='transactions.companytransaction')),
            ],
        ),
        migrations.CreateModel(
            name='CardSpending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_transactions', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='transactions.companytransaction')),
                ('restaurant_transactions', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='transactions.restauranttransaction')),
            ],
        ),
    ]
