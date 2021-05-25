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

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null= True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null= True, blank=True)

    class Meta:
        abstract = True
    

class Profile(TimeStampedModel):

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.PointField()
    email = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_images')
    #flipped_profile_photo = models.ImageField(upload_to='flipped_profile_images')
    is_active = models.BooleanField(default=True)
    match=models.ManyToManyField('self', through='ProfileMatch', symmetrical=False)

    class Meta:
        db_table = "Profiles"

    def __str___(self):
        return self.full_name

class ProfileMatch(TimeStampedModel):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user2")
    match_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user1', 'user2',)
        db_table = "profile_matches"

    def __str___(self):
        return self.user1.full_name,self.user2.full_name