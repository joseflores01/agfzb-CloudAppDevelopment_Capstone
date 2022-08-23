from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# - __str__ method to print a car make object
# class CarMake(models.Model):
#     car_name = models.CharField(null=False, max_length=20, primary_key=True)
#     car_description = models.TextField()

#     def __str__(self):
#         return self.car_name + " " + self.car_description
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=20)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return "Name: " + self.name




class CarModel(models.Model):

    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    # dealer_id = models.IntegerField()
    dealer_id = models.IntegerField(default=1, primary_key=True)
    name = models.CharField(null=False, max_length=20)

    # name = models.CharField(null=False, max_length=100, default='Car')

    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'

    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon')
    ]

    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )

    year = models.DateField()

    def __str__(self):
        return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
