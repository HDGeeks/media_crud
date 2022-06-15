from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework import status

from .serializers import ArtistSerializer 
from .models import Artist 

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides basic crud 
    operations for artist table .
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes=['AllowAny',]




