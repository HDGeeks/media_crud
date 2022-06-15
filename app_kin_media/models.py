from pyexpat import model
from django.db import models
from django.forms import DurationField
from django.utils import timezone
from core.settings import MEDIA_ROOT
from django.utils.translation import gettext_lazy as _

# Create your models here.





def artist_photo_directory_path(instance ,filename):
    # file will be uploaded to MEDIA_ROOT/artist_id_<id>/<filename>
        return 'artist_id_{0}/{1}'.format(instance.artist_id , filename)

def album_cover_directory(instance ,filename):
    # file will be uploaded to MEDIA_ROOT/artist_id_<id>/<filename>
        return 'album_id_{0}/{1}'.format(instance.artist_id , filename)

class Artist(models.Model):

    artist_id=models.AutoField(primary_key=True)
    artist_name=models.CharField(max_length=255 ,default=_(
    "unknown"),null=False ,blank=False)
    artist_photo = models.ImageField(upload_to=artist_photo_directory_path, height_field=None, width_field=None, max_length=100)
    artist_description=models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['artist_id']


    def __str__(self):
        return self.artist_name




class Album(models.Model):

    Genre= (
        (0, _('reggea')),
        (1, _('hip-hop')),
        (2, _('pop')),
        (3, _('soul')),
        (4, _('RnB'))
    )
    album_id=models.AutoField(primary_key=True)
    artist = models.ForeignKey(
        Artist ,related_name='album_artist_id', default=1 , on_delete=models.DO_NOTHING)
    album_genre = models.IntegerField(
        choices=Genre, default=0, verbose_name=_("Genre"))

    album_name=models.CharField(max_length=255 , null=False , blank= False ,default='unknown')
    album_cover = models.ImageField(upload_to=album_cover_directory, height_field=None, width_field=None, max_length=100)
    album_description=models.CharField(max_length=255 , null=False , blank=False ,default= "name")
    album_release_date=models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['album_id']

    def __str__(self):
        return self.album_name , self.album_release_date , self.album_genre

    
class Track(models.Model):

    track_id=models.AutoField(primary_key=True)
    artist = models.ForeignKey(
        Artist , default=1 , on_delete=models.DO_NOTHING)
    album = models.ForeignKey(
        Album,related_name='track_album_id', default=1 , on_delete=models.DO_NOTHING)
    #music_cover = models.ForeignKey(
      # Album ,related_name='track_album_cover', default=1 , on_delete=models.DO_NOTHING)
    track_description=models.CharField(max_length=100)
    track_name= models.CharField(max_length=50 , null=False ,blank=False)
    track_file = models.FileField(upload_to='' , null=True)
    duration=DurationField()

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['track_id']


    def __str__(self):
        return self.track_name ,self.track_file ,self.track_file
        


