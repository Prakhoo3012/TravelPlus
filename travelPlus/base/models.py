from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

meals_choices = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
)

class Country(models.Model):
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return self.country_name
    
class City(models.Model):
    city_name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
    

class Packages(models.Model):
    package_name = models.TextField(null=False, blank=False)
    package_description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=False, blank=False)
    price = models.IntegerField()
    destination = models.ForeignKey(City, on_delete=models.CASCADE)
    accomodation_type = models.TextField(null=True, blank=True)
    transportation_type = models.TextField(null=True, blank=True)
    meals = MultiSelectField(choices=meals_choices, max_length=64)
    tour_guide = models.BooleanField(default=True)
    inclusions = models.TextField(blank=True)
    exclusions = models.TextField(blank=True)
    availability = models.DateField()


    def __str__(self):
        return self.package_name