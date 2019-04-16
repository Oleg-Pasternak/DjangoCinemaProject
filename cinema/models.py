from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Movie(models.Model):
    """
        Class to store movies
    """
    # Fields
    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=2,
                                 decimal_places=1,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(10)])
    runtime = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    background = models.ImageField(upload_to='backgrounds/')
    video = models.URLField(max_length=180)

    # How object will be displayed in admin page
    def __str__(self):
        return "{} {}".format(self.title, self.year)

    def get_absolute_url(self):
        return reverse('cinema:movie_detail', args=[self.pk, ])
