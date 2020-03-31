from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=128)
    DOB = models.DateField()
    Bio = models.CharField(max_length=800)
    def __str__(self):
        return self.name

    def avg_rating(self):
        sum=0
        for song in self.song_set.all():
            ratings = Rating.objects.filter(song=song)
            sum = sum + song.avg_rating()
        if len(self.song_set.all()) > 0:
            return sum/len(self.song_set.all())
        else:
            return 0


class Song(models.Model):
    name = models.CharField(max_length=200)
    Date_of_release = models.DateField()
    cover = models.ImageField(upload_to='song_covers')
    artist = models.ManyToManyField(Artist)
    def __str__(self):
        return self.name

    def no_of_ratings(self):
        ratings = Rating.objects.filter(song=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(song=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        constraints = [
        models.UniqueConstraint(fields= ['song','user'], name='unique_rating'),
        ]