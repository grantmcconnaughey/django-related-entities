========
Usage
========

At the heart of django-related-entities is the ``RelatedEntity`` model. This model is used to relate the two objects in your Django app. The ``RelatedEntity`` model stores a ``primary_object`` and a ``related_object``, and optionally a ``role`` (which is a ``CharField``).

To add a related entity record, use the ``add_related`` function under ``relatedentities.utils``::

    from relatedentities.utils import add_related
    from my_app.models import Cat, Dog

    user = User.objects.get(username="catlover123")
    cat = Cat.objects.get(name="Cat")

    add_related(user, cat, "Owner")

This will add a ``RelatedEntity`` record where the user is the ``primary_object``, the cat is the ``related_object``, and the role field is set to ``"Owner"``.

++++++++++++++++++++++++++
Retrieving RelatedEntities
++++++++++++++++++++++++++

Let's make ``user`` be related to a few more cats and dogs in our database::

    from relatedentities.utils import add_related
    from my_app.models import Cat, Dog, User

    user = User.objects.get(username="catlover123")
    dog1 = Dog.objects.all()[0]
    dog2 = Dog.objects.all()[1]
    dog3 = Dog.objects.all()[2]

    add_related(user, dog1)
    add_related(user, dog2)
    add_related(user, dog3)

To later retrieve the related entities for ``user``, you can use the custom manager methods that come with ``RelatedEntity``::

    related_entities = RelatedEntity.objects.by_primary(user)

This will return a list of 4 ``RelatedEntity`` objects (1 where cat is the ``related_object`` and 3 where the dogs are the ``related_object``). To display this list in a template, you could loop through and output all of the ``related_object`` fields.::

    {% for entity in related_entities %}
        {{ entity.related_object }}
    {% endfor %}


+++++++++++++++++++++++++
Determining Relationships
+++++++++++++++++++++++++

django-related-entities is handy when used with authorization (i.e. Is User ``user`` related to ``Company`` company?). A useful mixin class called ``RelatedEntityMixin`` can be added to your models. It supplies the ``is_related_to`` method to determine relationships::

    class Cat(RelatedEntityMixin, models.Model):

        name = models.CharField(max_length=255)

    dog = Dog.objects.first()
    cat = Cat.objects.first()

    add_related(cat, dog)

    assert cat.is_related_to(dog)
    assert user.is_related_to(dog) is False
