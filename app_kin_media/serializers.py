from rest_framework import serializers
from .models import Artist , Album , Track

from rest_framework import status
from rest_framework.response import Response


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["track_id","track_name","track_file"]

    """  def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   
    def perform_create(self, serializer):
        serializer.save()
     """

class AlbumSerializer(serializers.ModelSerializer):
    track_list = TrackSerializer(many=True , required=True)

    class Meta:
        model = Album
        fields = ["album_id","album_name ","track_list"]

"""     def create(self, validated_data):
        # gets our 
        tracks_data = validated_data.pop('track_id')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def perform_create(self, serializer):
        serializer.save() """

class ArtistSerializer(serializers.ModelSerializer):
    album_list = AlbumSerializer(many=True , required=True)

    class Meta:
        model = Artist
        fields = ["artist_id" ,"artist_name" ,"album_list"]

    """ def create(self, validated_data):
        # get the album
        albums_data = validated_data.pop('album_list')
       
        # create our artist based on artist_id serializer
        artist_data = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=artist_data, **album_data)
        return artist_data
    def perform_create(self, serializer):
        serializer.save() """

    def create(self, validated_data):
        albums_data = validated_data.pop('album_list')
        artist_data = Artist.objects.create(**validated_data)

        for album_data in albums_data:
            tracks_data = album_data.pop('track_list')
            album_data = Album.objects.create(artist_id=artist_data ,**album_data)

            for track_data in tracks_data:
                Track.objects.create(album_id=album_data ,**track_data)
        return artist_data

    
