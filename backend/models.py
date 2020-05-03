from django.db import models

# Create your models here.

class Grocery(models.Model):
    groceryId = models.IntegerField(primary_key=True, null=False, default=0)
    name = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255)
    expirationDate = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    expiredStatus = models.IntegerField()
    pantryStatus = models.IntegerField()

    def __str__(self):
        return self.name

class Pantry(models.Model):
    pantryId = models.IntegerField(primary_key=True, null=False, default=0)
    name = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255)
    expirationDate = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    expiredStatus = models.IntegerField()
    pantryStatus = models.IntegerField()

    def __str__(self):
        return self.name

class Trends(models.Model):
    name = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    expiredStatus = models.IntegerField()
    pantryStatus = models.IntegerField()
    month = models.CharField(max_length=255)

    def __str__(self):
        return self.name

