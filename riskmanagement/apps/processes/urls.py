from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('company-site', views.CompanySiteViewSet)
router.register('process-types', views.ProcessTypeViewSet)
router.register('processes', views.ProcessViewSet)
router.register('players', views.PlayerViewSet)
router.register('process-players', views.ProcessPlayerViewSet)
router.register('io-elements', views.IOElementViewSet)
router.register('process-io', views.ProcessIOViewSet)
router.register('statusProcess', views.StatusProcessViewSet)