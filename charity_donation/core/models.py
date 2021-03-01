from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']


class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    TYPES = (
        (1, "Fundacja"),
        (2, "Organizacja pozarządowa"),
        (3, "Zbiórka lokalna"),
    )
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default=1,
    )
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-id']


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)  # ulica + nr domu - nie dawać 100
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.IntegerField()  # nie jestem pewien TimeField
    pick_up_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)  # foringki

    class Meta:
        ordering = ['-id']

# metoda fetch do JS z wysyłaniem darów
# doczytać o settings.AUTH_USER_MODEL
# get user model wszędzie indziej.
