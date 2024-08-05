import os
from django.utils.deconstruct import deconstructible

@deconstructible
class RoomImageRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Rename the file to the room number
        filename = f'{instance.hotel.hotel_number}-{instance.room_number}.{ext}'
        # Return the whole path to the file
        return os.path.join(self.path, filename)


@deconstructible
class HotelImageRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Rename the file to the room number
        filename = f'{instance.hotel_number}.{ext}'
        # Return the whole path to the file
        return os.path.join(self.path, filename)
