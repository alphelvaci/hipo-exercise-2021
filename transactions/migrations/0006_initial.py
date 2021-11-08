# Generated by Django 3.2.9 on 2021-11-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0005_employee_contract_type'),
        ('transactions', '0005_auto_20211108_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFundingTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
        migrations.AddConstraint(
            model_name='companyfundingtransaction',
            constraint=models.CheckConstraint(check=models.Q(('amount__gt', 0)), name='amount_gt_0'),
        ),
    ]