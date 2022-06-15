from django.contrib import admin
from django.db import models

from .models import Artist , Album , Track
# Register your models here.


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)

""" 
@admin.register(Artist)
class ArtistAdmin(admin.TabularInline):
	list_display = [
        'artist_name',
        'artist_photo',
        ]
@admin.register(Album)
class AlbumInlineModel(admin.TabularInline):
    model = Artist
    fields = [
        'album_name', 
        'album_genre',
        'album_release_date'

        ]


@admin.register(Track)
class TrackAdmin(admin.TabularInline):
    model: Album
    fields = [
        'track_name',
        'album',
        ]
    list_display = [
        'artist', 
       
        ]
    inlines = [
        AlbumInlineModel, 
        ]  

 """

