from unittest import TestCase
from .models import Cat, Dog
from relatedentities.models import RelatedEntity
from relatedentities.utils import add_related


class RelatedEntityModelTests(TestCase):

    def test_delete_removes_both_sides_of_relationship(self):
        cat = Cat.objects.create(name='Test Cat')
        dog = Dog.objects.create(name='Test Dog')

        related = add_related(cat, dog)
        rev_related = add_related(dog, cat)

        related.delete()

        self.assertFalse(RelatedEntity.objects.filter(pk=related.pk).exists())
        self.assertFalse(RelatedEntity.objects.filter(pk=rev_related.pk).exists())

    def test_is_related_to(self):
        cat = Cat.objects.create(name='Test Cat')
        dog = Dog.objects.create(name='Test Dog')

        related = add_related(cat, dog)

        self.assertTrue(cat.is_related_to(dog))

    def test_is_related_to_works_with_reverse_relationship(self):
        cat = Cat.objects.create(name='Test Cat')
        dog = Dog.objects.create(name='Test Dog')

        related = add_related(cat, dog)

        self.assertTrue(dog.is_related_to(cat))

    def test_is_related_to_works_with_reverse_relationship(self):
        cat = Cat.objects.create(name='Test Cat')
        dog = Dog.objects.create(name='Test Dog')

        self.assertFalse(cat.is_related_to(dog))
