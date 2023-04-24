from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import Role
from .models import Profile
from .models import Group
from .models import UserAssign

#from .models import StructureWebsite, SubStructure
from .models import Permissions
from .models import WebsiteStructure

from .models import DataLog
admin.site.register(DataLog)

class PermAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'structure_id','read', 'create', 'edit','erase')

class RoleAdmin(TreeAdmin):
    form = movenodeform_factory(Role)

admin.site.register(Role, RoleAdmin)

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(UserAssign)

admin.site.register(WebsiteStructure)

admin.site.register(Permissions, PermAdmin)
