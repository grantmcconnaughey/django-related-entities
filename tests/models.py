from django.db import models
from relatedentities.models import RelatedEntityMixin


class Cat(RelatedEntityMixin, models.Model):

    name = models.CharField(max_length=255)


class Dog(RelatedEntityMixin, models.Model):

    name = models.CharField(max_length=255)
