from rest_framework import routers
from .api import ContactViewSet

router = routers.DefaultRouter()
router.register('api/mycontacts', ContactViewSet, 'mycontacts')

urlpatterns = router.urls