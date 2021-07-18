from django.db import models

# Create your models here.
#  Every model is going to be a python class.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    # on_delete -> if we delete the airport(ex:JFK) from airports table, we also delete the flight
    # we can also prevent deleting airport if any flight fly from or to the airport (models.protect)
    # related name -> a way of me accessing a relationship in a reverse order
    # ex: I want to see all flights have that airport as an origin.
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"
    # This define the string representation of the obj.

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
