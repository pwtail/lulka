from django.db import models
from django.db.models import Manager
from vinyl.qs import VinylManager

class Brand(models.Model):
    name = models.CharField(max_length=100)

    vinyl = VinylManager()

class Title(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100)


class Async:
    async def save(self):
        print(1)


class M(Async, models.Model):
    title = models.ForeignKey(Title, on_delete=models.DO_NOTHING, null=True)
    x = models.IntegerField()
    brands = models.ManyToManyField(Brand)

    vinyl = VinylManager()
    objects = Manager()

    def V(self):
        1


    # @branch
    # async def save(self):
    #     1