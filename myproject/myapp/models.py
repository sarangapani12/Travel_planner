from django.db import models
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)  # e.g. "IN", "FR"
    flag_emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    cover_image = models.URLField(blank=True)
    latitude = models.FloatField(null=True, blank=True)   # ADD THIS
    longitude = models.FloatField(null=True, blank=True)  # ADD THIS
    budget_level = models.CharField(max_length=20, default='medium',
        choices=[('budget','Budget'),('medium','Medium'),('luxury','Luxury')])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Temple", "Museum", "Beach"
    icon = models.CharField(max_length=10, blank=True)  # emoji icon

    def __str__(self):
        return self.name

class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    cover_image = models.URLField(blank=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True)
    entry_fee = models.CharField(max_length=100, blank=True)
    tips = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    url = models.URLField()
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.place.name} - image"