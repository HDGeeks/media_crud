from app_kin_media.views import ArtistViewSet 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'artist', ArtistViewSet)

urlpatterns = router.urls
