from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework import status

from .serializers import ArtistSerializer , AlbumSerializer ,TrackSerializer
from .models import Artist , Album ,Track

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides basic crud 
    operations for artist table .
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides basic crud 
    operations for album table .
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides basic crud 
    operations for track table .
    """
    queryset = Track.objects.all()
    serializer_class = ArtistSerializer

