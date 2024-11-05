from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    title = models.CharField(max_length=150)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.title}"
