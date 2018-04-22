from django.db import models


# Create your models here.
class FibonacciNumber(models.Model):
    number = models.BigIntegerField(unique=True)
    value = models.BigIntegerField()

    class Meta:
        db_table = "fibonacci_numbers"