# Generated by Django 3.2.9 on 2021-11-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_cardrestauranttransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardrestauranttransaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='companycardtransaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='companyfundingtransaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
