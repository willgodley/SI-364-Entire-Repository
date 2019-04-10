from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)
    region_id = models.ManyToManyField('Region', through = 'Site')
    states_id = models.ManyToManyField('States', through = 'Site')


    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=128)
    region_id = models.ManyToManyField('Region', through = 'Site')
    category_id = models.ManyToManyField('Category', through = 'Site')

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)
    states_id = models.ManyToManyField('States', through = 'Site')
    category_id = models.ManyToManyField('Category', through = 'Site')

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)
    states_id = models.ManyToManyField('States', through = 'Site')


    def __str__(self) :
        return self.name


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
