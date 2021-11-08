from django.db import models
from companies.models import Company, Card
from restaurants.models import Restaurant

# Create your models here.


class CompanyFundingTransaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)  # up to 999 millon
    date = models.DateTimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(amount__gt=0), name='amount_gt_0'),
        ]

    def __str__(self):
        return f"Funding {self.id} ({self.company} +{self.amount})"
