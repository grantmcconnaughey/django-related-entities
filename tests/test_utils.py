from django.test import TestCase
from relatedentities.models import RelatedEntity
from relatedentities.utils import add_related
from .models import Cat, Dog


class RelatedEntitiesUtilsTests(TestCase):

    def setUp(self):
        self.cat = Cat.objects.create(name="Test Cat")
        self.dog = Dog.objects.create(name="Test Dog")

    def test_add_related_adds_one_record(self):
        related_entity = add_related(self.cat, self.dog)

        self.assertEqual(RelatedEntity.objects.count(), 1)

    def test_add_related_returns_instance_of_related_entity(self):
        related_entity = add_related(self.cat, self.dog)

        self.assertIsInstance(related_entity, RelatedEntity)
