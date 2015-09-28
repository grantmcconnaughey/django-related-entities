from django.contrib import admin
from .models import RelatedEntity


class RelateEntityModelAdmin(admin.ModelAdmin):
    list_display = ("id", "primary_content_type", "primary_object",
                    "primary_object_id", "content_type", "related_object",
                    "object_id", "role")
    search_fields = ("id", "primary_content_type__model",
                     "content_type__model", "role", "primary_object_id",
                     "object_id")
    list_per_page = 25


admin.site.register(RelatedEntity, RelateEntityModelAdmin)
