from django.contrib import admin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import ProcessType, Process, Player, IOElement, ProcessPlayer, ProcessIO, CompanySite,StatusProcess


class ProcessAdmin(TreeAdmin):
    form = movenodeform_factory(Process)

class PlayerAdmin(TreeAdmin):
    form = movenodeform_factory(Player)

class ProcessTypesAdmin(TreeAdmin):
    form = movenodeform_factory(ProcessType)


admin.site.register(CompanySite)
admin.site.register(ProcessType, ProcessTypesAdmin)
admin.site.register(Process)
admin.site.register(Player, PlayerAdmin)
admin.site.register(IOElement)
admin.site.register(ProcessPlayer)
admin.site.register(ProcessIO)
admin.site.register(StatusProcess)