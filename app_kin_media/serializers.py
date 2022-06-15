from rest_framework import serializers
from .models import Artist , Album , Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    track_album_id = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"

    def create(self, validated_data):
        tracks_data = validated_data.pop('track_album_id')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

class ArtistSerializer(serializers.ModelSerializer):
    album_artist_id = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = "__all__"

    def create(self, validated_data):
        albums_data = validated_data.pop('album_artist_id')
        artist = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=artist, **album_data)
        return artist
