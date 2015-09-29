from django.test import TestCase
from relatedentities.models import RelatedEntity
from relatedentities.utils import add_related
from .models import Cat, Dog


class RelatedEntityManagerTests(TestCase):

    def setUp(self):
        self.cat = Cat.objects.create(name="Test Cat")
        self.dog = Dog.objects.create(name="Test Dog")

    def test_by_primary_entity_returns_related_models(self):
        add_related(self.cat, self.dog)

        entities = RelatedEntity.objects.by_primary(self.cat)

        self.assertEqual(len(entities), 1)
        self.assertEqual(entities.first().primary_object, self.cat)
        self.assertEqual(entities.first().related_object, self.dog)
