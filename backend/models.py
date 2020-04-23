from django.db import models

# Create your models here.

class Grocery(models.Model):
    idNo = models.CharField(primary_key=True,max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    exp_time = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name