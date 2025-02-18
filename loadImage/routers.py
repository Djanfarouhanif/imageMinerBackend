from rest_framework import routers
from .views import LoadViewset

router = routers.DefaultRouter()

router.register(r'load',LoadViewset, basename='load')
urlpatterns = router.urls