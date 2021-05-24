from django.utils.timezone import now
from django.contrib.gis.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

PROFILE_MATCH_CHOICES = (
    ('Pending', 'pending'),
    ('Rejected', 'rejected'),
    ('Matched', 'matched'),
)

class Profile(models.Model):

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.PointField()
    email = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_images')
    flipped_profile_photo = models.ImageField(upload_to='flipped_profile_images')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False) #` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_at = models.DateTimeField(default=now) #` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',

    class Meta:
        db_table = "profiles"

    def __str___(self):
        return self.full_name

class ProfileMatch(models.Model):

    requested_profile = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name='requested_profile')
    match_profile = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name='match_profile')
    match_status = models.CharField(max_length=100, choices=PROFILE_MATCH_CHOICES)
    created_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False) #` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_at = models.DateTimeField(default=now) #` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',


    class Meta:
        db_table = "profile_matches"

    def __str___(self):
        return self.full_name