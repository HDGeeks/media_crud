from rest_framework import serializers
from .models import Artist , Album , Track

from rest_framework import status
from rest_framework.response import Response


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   
    def perform_create(self, serializer):
        serializer.save()
    

class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True , required=True)

    class Meta:
        model = Album
        fields = "__all__"

    def create(self, validated_data):
        # gets our 
        tracks_data = validated_data.pop('track_id')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def perform_create(self, serializer):
        serializer.save()

class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True , required=True)

    class Meta:
        model = Artist
        fields = "__all__"

    def create(self, validated_data):
        # get the album
        albums_data = validated_data.pop('album_id')
        print(albums_data)
        # create our artist based on artist_id serializer
        artist = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=artist, **album_data)
        return artist 
    def perform_create(self, serializer):
        serializer.save()
