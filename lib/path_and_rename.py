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
        filepath = f"media/room_images/{filename}"
        if os.path.exists(filepath):
            os.unlink(filepath)
        # Return the whole path to the file
        return os.path.join(self.path, filename)


@deconstructible
class HotelImageRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Rename the file to the hotel number
        filename = f'{instance.hotel_number}.{ext}'
        filepath = f"media/hotel_images/{filename}"
        if os.path.exists(filepath):
            os.unlink(filepath)
        # Return the whole path to the file
        return os.path.join(self.path, filename)


@deconstructible
class ProfileImageRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Rename the file to the username
        filename = f'{instance.user.username}.{ext}'
        filepath = f"media/profile_pics/{filename}"
        
        if os.path.exists(filepath):
            os.unlink(filepath)
        # Return the whole path to the file
        return os.path.join(self.path, filename)

    

@deconstructible
class EventCenterImageRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Rename the file to the event center number
        filename = f'{instance.event_center_number}.{ext}'
        filepath = f"media/event_center_images/{filename}"
        if os.path.exists(filepath):
            os.unlink(filepath)
        # Return the whole path to the file
        return os.path.join(self.path, filename)

