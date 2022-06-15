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

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['artist_id']


    artist_id=models.AutoField(primary_key=True)
    artist_name=models.CharField(max_length=255 ,default=_(
    "unknown"),null=False ,blank=False)
    artist_photo = models.ImageField(upload_to=artist_photo_directory_path, height_field=None, width_field=None, max_length=100)
    artist_description=models.CharField(max_length=100)


    def __str__(self):
       return f'{self.artist_id} {self.artist_name}'




class Album(models.Model):
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['album_id']

    Genre= (
        ("reggea",'reggea'),
        ("hip-hop",'hip-hop'),
        ("pop",'pop'),
        ("solo",'solo'),
        ("RnB", 'RnB'),
    )
    album_id=models.AutoField(primary_key=True)
    
    album_genre = models.CharField(max_length=255 ,
        choices=Genre, default="pop", verbose_name=_("Genre"))

    album_name=models.CharField(max_length=255 , null=False , blank= False ,default='collection')
    album_cover = models.ImageField(upload_to=album_cover_directory, height_field=None, width_field=None, max_length=100)
    album_description=models.CharField(max_length=255 , null=False , blank=False ,default= "name")
    album_release_date=models.DateTimeField(auto_now_add=True,)
    artist_id = models.ForeignKey(
        Artist ,related_name='album_artist_id', on_delete=models.DO_NOTHING)

    

    def __str__(self):
           return f'{self.album_id} {self.album_name}'

    
class Track(models.Model):

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['track_id']

    track_id=models.AutoField(primary_key=True)
   
   
    track_description=models.CharField(max_length=100)
    track_name= models.CharField(max_length=50 , null=False ,blank=False)
    track_file = models.FileField(upload_to='' , null=True)
    duration=DurationField()

    trackalbum_id= models.ForeignKey(
    Album,related_name='track_album_id', on_delete=models.DO_NOTHING)
    #trackartist_id= models.ForeignKey(
    #Artist,related_name='track_artist_id', on_delete=models.DO_NOTHING)

    

  
    def __str__(self):
        return f'{self.track_id} {self.track_name} {self.track_file}'
        


