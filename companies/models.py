from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Company(models.Model):
    name = models.CharField(max_length=45)
    employees = models.ManyToManyField(Employee)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return f"{self.name}"


class Card(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.employee}'s Card (Card {self.id})"
