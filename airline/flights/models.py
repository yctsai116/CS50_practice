from django.db import models

# Create your models here.
#  Every model is going to be a python class.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"
    # This define the string representation of the obj.