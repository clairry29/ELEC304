from django.db import models

# Parent Model
class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {self.price}"


# Child Model 1
class Car(Vehicle):
    doors = models.IntegerField()

    # Method Overriding
    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {self.price}"


# Child Model 2
class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=False)

    # Method Overriding
    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self.price}"