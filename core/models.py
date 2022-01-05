from random import randint

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.fields import BooleanField, CharField, DurationField, PositiveSmallIntegerField, SmallIntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class UserProfileInfo(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

#################################################

class Thing(models.Model):
    name = CharField(max_length=64)
    short_description = TextField()
    long_description = TextField()
    address = CharField(max_length=128)
    stars = PositiveSmallIntegerField(null=True,
        blank=True)

    categories = ['Attraction', 'Tour']
    tuple_categories = [(c.lower().replace(' ', '_'), c) for c in categories]
    category = CharField(max_length=64, choices=tuple_categories)
    covid_safe = BooleanField()

    def get_picture(self):
        pictures = self.picture_set.all()
        if len(pictures):
            return pictures[randint(0, len(pictures)-1)]

    def __str__(self):
        return f"{self.name} | {self.category}"

class Attraction(Thing):
    types = ['Nightlife', 'Sight', 'Landmark', 'Museum', 'Fun']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    good_fors = ['Kids', 'Big Groups',
        'Adrenaline Seekers',
        'a Rainy Day', 'Couples']
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_fors]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def get_absolute_url(self):
        return reverse("core:attraction_detail", kwargs={"pk": self.pk})

class Tour(Thing):
    category = 'Tour'

    types = ['Multi-day', 'City', 'Cultural', 'Historical', 'Hicking']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    price = SmallIntegerField()
    duration = DurationField()

class Picture(models.Model):
    thing = ForeignKey(Thing, on_delete=models.CASCADE)
    image = ImageField(upload_to='thing_pics')

    def get_absolute_url(self):
        return reverse(f"core:{self.thing.category.lower()}_detail", kwargs={"pk": self.thing.pk})

#################################################

class Plan(models.Model):
    owner = ForeignKey(User, on_delete=models.CASCADE)

class PlanThing(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    plan = ForeignKey(Plan, on_delete=models.CASCADE)
    
#################################################