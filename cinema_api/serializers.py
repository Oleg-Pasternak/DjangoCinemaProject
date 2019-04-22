from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'image', 'get_absolute_url', 'year', 'rating')
