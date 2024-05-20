from django.contrib import admin
from .models import Country, City, Packages, Customer

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Packages)
admin.site.register(Customer)
