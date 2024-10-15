from django.contrib import admin
from .models import Hotel, Room, Amenity, RoomAmenity, Booking

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(RoomAmenity)
admin.site.register(Booking)
# Register your models here.
