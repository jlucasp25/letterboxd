from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f'{self.title} ({self.year})'
