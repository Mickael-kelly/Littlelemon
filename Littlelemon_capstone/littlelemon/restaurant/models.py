from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f"{self.title} : {self.price}"

class Booking(models.Model):
    names = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()