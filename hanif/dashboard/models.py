from django.db import models

# Create your models here.
class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    item_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.item_name