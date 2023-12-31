from django.db import models


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=30)
    symbols = models.CharField(max_length=10, default='NO')
    price = models.FloatField(default=0)
    change_price = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    image = models.ImageField(upload_to='images/curr/')

    def __str__(self):
        return self.name
