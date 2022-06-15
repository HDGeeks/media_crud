# Generated by Django 4.0.1 on 2022-06-14 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_kin_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_genre',
            field=models.IntegerField(choices=[(0, 'reggea'), (1, 'hip-hop'), (2, 'pop'), (3, 'soul'), (4, 'RnB')], default=0, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='album_artist_id', to='app_kin_media.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='track_album_id', to='app_kin_media.album'),
        ),
    ]
