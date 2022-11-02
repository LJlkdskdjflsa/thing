import pytest

# from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Tag, Space, Thing

# from utils.tests.conftest import ConfTest


@pytest.mark.django_db
class TagModelTest(TestCase):
    def test_tag_create(self):
        new_tag = Tag()
        new_tag.title = "new_tag"
        new_tag.save()
        assert new_tag.title == "new_tag"

    def test_tag_read(self):
        new_tag = Tag()
        new_tag.title = "new_tag"
        new_tag.save()
        assert new_tag.title == "new_tag"


@pytest.mark.django_db
class SpaceModelTest(TestCase):
    def test_space_model_persists(self):
        new_space = Space.objects.create(title="new_space")
        assert new_space.title == "new_space"


class ThingModelTest(TestCase):
    @pytest.mark.django_db
    def test_tag_model_persists(self):
        new_thing = Thing()
        new_thing.title = "new_thing"
        new_thing.save()
        assert new_thing.title == "new_thing"
