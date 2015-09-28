from django.db import models
from relatedentities.models import RelatedEntityMixin


class Cat(models.Model, RelatedEntityMixin):

    name = models.CharField(max_length=255)


class Dog(models.Model, RelatedEntityMixin):

    name = models.CharField(max_length=255)
