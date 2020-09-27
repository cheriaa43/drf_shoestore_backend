from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=100)
    
    def __str__(self):
        return self.style


"""
Joe, much like Tarzan, grew up amongst a variety of wildlife. Growing up in the African Savannah and being atop the food chain gave him extensive hunting skills and sharp intuitions. Wehn he was approaching adulthood, poachers found him dressed in zebra hide and brought him to the United States where he decided to use technology to bridge the gap between animals and humans in his childhood home through speech to text translations of animal languages.
"""


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name
