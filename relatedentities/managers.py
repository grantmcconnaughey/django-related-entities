from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q


class RelatedEntityManager(models.Manager):

    def by_primary_entity(self, entity):
        content_type = ContentType.objects.get_for_model(entity)
        return self.filter(primary_content_type=content_type,
                           primary_object_id=entity.pk)

    def by_primary_entity_and_type(self, entity, content_type):
        return self.filter(primary_content_type=content_type,
                           primary_object_id=entity.pk)

    def by_related_entity(self, entity):
        content_type = ContentType.objects.get_for_model(entity)
        return self.filter(Q(primary_content_type=content_type,
                             primary_object_id=entity.pk) |
                           Q(related_content_type=content_type,
                             related_object_id=entity.pk))

    def by_primary_and_related(self, primary, related):
        primary_content_type = ContentType.objects.get_for_model(primary)
        related_content_type = ContentType.objects.get_for_model(related)
        return self.filter(Q(primary_content_type=primary_content_type,
                             primary_object_id=primary.pk) |
                           Q(related_content_type=related_content_type,
                             related_object_id=related.pk))
