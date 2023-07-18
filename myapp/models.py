from django.db import models

# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=250)
    model=models.CharField(max_length=200)
    category=models.CharField(max_length=230)
    owner_type=models.CharField(max_length=200)
    fual_type=models.CharField(max_length=200)
    kms=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=2550)
    number=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    name=models.CharField(max_length=250)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    display=models.CharField(max_length=200,default="lcd")

    def __str__(self):
        return self.name
    

class Movies(models.Model):
    name=models.CharField(max_length=250)
    genre=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    language=models.CharField(max_length=250)
    rate=models.PositiveIntegerField()

    def __str__(self):
        return self.name


    