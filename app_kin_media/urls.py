from app_kin_media.views import ArtistViewSet ,AlbumViewSet ,TrackViewSet
from rest_framework import renderers
from django.urls import path, include , re_path


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)
urlpatterns = router.urls
