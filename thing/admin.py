from django.contrib import admin
from .models import Tag, Space, Thing


from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm


class SpaceAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    form = TreeNodeForm


admin.site.register(Space, SpaceAdmin)
admin.site.register(Tag)
admin.site.register(Thing)
