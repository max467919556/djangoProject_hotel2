# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hotel Name")
    location = models.CharField(max_length=200, verbose_name="Location")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3, verbose_name="Rating")
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, unique=True, verbose_name="Room Number")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    amenities = models.ManyToManyField('Amenity', through='RoomAmenity')

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"

class Amenity(models.Model):
    name = models.CharField(max_length=50, verbose_name="Amenity Name")
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name

class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Room Amenity"
        verbose_name_plural = "Room Amenities"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room}"

    def total_price(self):
        return (self.check_out - self.check_in).days * self.room.price_per_night


from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)