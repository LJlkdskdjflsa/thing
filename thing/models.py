from django.db import models
from treenode.models import TreeNodeModel
from django.contrib.auth.models import User


class Tag(models.Model):
    """tags of all space and thing"""

    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "tags"


class Space(TreeNodeModel):
    treenode_display_field = "title"
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="spaces"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="spaces")
    metadata = models.JSONField(default=dict, blank=True, null=True)

    @property
    def _metadata(self):
        return self.metadata

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Space"
        verbose_name_plural = "Space"


class Thing(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="things"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="things")
    space = models.ForeignKey(
        Space, on_delete=models.SET_NULL, blank=True, null=True, related_name="things"
    )
    metadata = models.JSONField(default=dict, blank=True, null=True)

    @property
    def _metadata(self):
        return self.metadata

    class Meta:
        verbose_name = "Thing"
        verbose_name_plural = "Things"
