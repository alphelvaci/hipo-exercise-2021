from django.contrib import admin
from .models import CompanyFundingTransaction, CompanyCardTransaction, CardRestaurantTransaction

# Register your models here.

admin.site.register([CompanyFundingTransaction, CompanyCardTransaction, CardRestaurantTransaction])
