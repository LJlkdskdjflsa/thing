from django.db import models

from treenode.models import TreeNodeModel


class OwnableTreeNodeTagBaseModel(TreeNodeModel):

    treenode_display_field = "name"

    title = models.CharField(max_length=50)

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        abstract = True
