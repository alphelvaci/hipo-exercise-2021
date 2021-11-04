from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name}"
