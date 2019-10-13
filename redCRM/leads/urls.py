from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/myleads', LeadViewSet, 'myleads')

urlpatterns = router.urls