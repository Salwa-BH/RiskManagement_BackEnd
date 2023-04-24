from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('datalog',views.DataLogViewSet)
router.register('role',views.RoleViewSet)
router.register('profile', views.ProfileViewSet)
router.register('group',views.GroupViewSet)
router.register('user-assign',views.UserAssignViewSet)
router.register('website-structure',views.WebsiteStructureViewSet)
router.register('profile-permissions',views.PermissionsViewSet)


