from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class ManufacturerType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Manufacturer(models.Model):

    name = models.CharField(max_length=20)
    type = models.ForeignKey(ManufacturerType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class FlavourType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Flavour(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='flavour', on_delete=models.CASCADE)
    flavour_type = models.ManyToManyField(FlavourType)
    flavour_name = models.CharField(max_length=30)
    in_stock = models.BooleanField()
    description = models.CharField(null=True, max_length=500, blank=True)
    add_time = models.DateField('date published')
    def __str__(self):
        return self.flavour_name

class BowlType(models.Model):
    type = models.CharField(max_length=15)
    def __str__(self):
        return self.type

class Bowl(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(BowlType, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Mix(models.Model):
    mix_name = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(default=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    strength = models.PositiveIntegerField(default=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    bowl = models.ForeignKey(Bowl, on_delete=models.CASCADE, null=True)
    description = models.CharField(null=True, max_length=500, blank=True)
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




