from pydoc import plain
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from ..prices.models import TimeStampedModel, Plan

class Coupon(models.Model):
    #plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    code = models.CharField(max_length= 7, unique= True)
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"


