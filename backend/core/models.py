from django.db import models

# Create your models here.
class HouseAddress(models.Model):
    # lat/long raw data
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # internal unique code (geohash / hashing)
    base_code = models.CharField(max_length=16, unique=True, db_index=True)

    # human readable prefix
    country = models.CharField(max_length=2)      # IN, US, etc...
    state = models.CharField(max_length=3)        # DL, MH, etc...

    # short plate-style number
    short_number = models.PositiveIntegerField()

    # final display code (IN-DL-10001)
    display_code = models.CharField(max_length=20, unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["display_code"]),
            models.Index(fields=["base_code"]),
        ]

    def __str__(self):
        return f"{self.display_code} ({self.latitude},{self.longitude})"