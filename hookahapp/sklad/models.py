from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Flavour(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='flavours', on_delete=models.CASCADE)
    flavour_name = models.CharField(max_length=30)
    in_stock = models.BooleanField()
    add_time = models.DateField('date published')
    def __str__(self):
        return self.flavour_name

class Mix(models.Model):
    mix_name = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    strength = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    compound = models.ManyToManyField(Flavour,
                                      through='Membership',
                                      )
    def __str__(self):
        return self.mix_name

class Membership(models.Model):
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    mix = models.ForeignKey(Mix, on_delete=models.CASCADE)
    def str(self):
        return str(self.flavour)




