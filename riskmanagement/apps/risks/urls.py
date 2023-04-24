from rest_framework.routers import DefaultRouter
from riskmanagement.apps.permissions.views import RoleViewSet,ProfileViewSet,GroupViewSet, UserAssignViewSet, WebsiteStructureViewSet,PermissionsViewSet,DataLogViewSet


router = DefaultRouter()


##

router.register('role',RoleViewSet)
router.register('profile', ProfileViewSet)
router.register('group',GroupViewSet)
router.register('user-assign',UserAssignViewSet)
router.register('website-structure', WebsiteStructureViewSet)
router.register('permissions', PermissionsViewSet)
router.register('datalog',DataLogViewSet)