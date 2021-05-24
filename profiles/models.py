from django.contrib.gis.db import models

from dj.choices import Choices, Choice
from dj.choices.fields import ChoiceField

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
from upside_town_app import  settings

class Profile(models.Model):

    full_name = models.CharField(max_length=100)
    location = models.PointField()
    email = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_images')

    class Meta:
        db_table = "profiles"

    def __str___(self):
        return self.full_name