from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields

from .managers import RelatedEntityManager


class RelatedEntity(models.Model):
    role = models.CharField(max_length=255, blank=True)

    primary_content_type = models.ForeignKey(ContentType, related_name="+")
    primary_object_id = models.PositiveIntegerField()
    primary_object = fields.GenericForeignKey('primary_content_type',
                                              'primary_object_id')

    related_content_type = models.ForeignKey(ContentType, related_name="+")
    related_object_id = models.PositiveIntegerField()
    related_object = fields.GenericForeignKey('related_content_type',
                                              'related_object_id')

    objects = RelatedEntityManager()

    def delete(self, **kwargs):
        super(RelatedEntity, self).delete()

        reverse_related = RelatedEntity.objects.filter(
            primary_content_type=self.related_content_type,
            primary_object_id=self.related_object_id,
            related_content_type=self.primary_content_type,
            related_object_id=self.primary_object_id)

        reverse_related.delete()


class RelatedEntityMixin(object):

    def is_related_to(self, entity):
        """
        Returns True if the current object has a RelatedEntity record relating
        itself to the entity parameter
        :param entity: The second entity to check in the RelatedEntity
        relationship
        :return: True if the two objects are related
        """
        if entity is None:
            return False

        self_content_type = ContentType.objects.get_for_model(self)
        entity_content_type = ContentType.objects.get_for_model(entity)
        return RelatedEntity.objects.filter(
            Q(primary_content_type=self_content_type,
              primary_object_id=self.pk,
              related_content_type=entity_content_type,
              related_object_id=entity.pk) |
            Q(primary_content_type=entity_content_type,
              primary_object_id=entity.pk,
              related_content_type=self_content_type,
              related_object_id=self.pk)).exists()
