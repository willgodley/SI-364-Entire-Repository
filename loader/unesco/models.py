from django.db import models

class Category(models.Model) :
    category = models.CharField(max_length=128)
    region = models.ManyToManyField('Region', through = 'Site')
    states = models.ManyToManyField('States', through = 'Site')

    def __str__(self) :
        return self.category

class States(models.Model) :
    state = models.CharField(max_length=128)
    category = models.ManyToManyField('Category', through = 'Site')
    region = models.ManyToManyField('Region', through = 'Site')

    def __str__(self) :
        return self.state

class Region(models.Model) :
    region = models.CharField(max_length=128)
    category = models.ManyToManyField('Category', through = 'Site')
    states = models.ManyToManyField('States', through = 'Site')

    def __str__(self) :
        return self.region

class Iso(models.Model) :
    iso = models.CharField(max_length=128)

    def __str__(self) :
        return self.iso


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    description = models.TextField()
    justification = models.TextField()
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)


    def __str__(self) :
        return self.name
