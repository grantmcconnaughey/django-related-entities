from django.contrib.contenttypes.models import ContentType

from .models import RelatedEntity


def add_related(primary_entity, related_entity, role=''):
    """Adds a related entity relationship if it does not exist."""

    primary_content_type = ContentType.objects.get_for_model(primary_entity)
    content_type = ContentType.objects.get_for_model(related_entity)

    try:
        related_entity = RelatedEntity.objects.get(
            related_content_type=content_type,
            related_object_id=related_entity.pk,
            primary_object_id=primary_entity.pk,
            primary_content_type=primary_content_type)
        return related_entity
    except RelatedEntity.DoesNotExist:
        related_entity = RelatedEntity(related_object=related_entity,
                                       primary_object=primary_entity,
                                       role=role)
        related_entity.save()
        return related_entity
