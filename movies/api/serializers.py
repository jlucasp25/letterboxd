from django.contrib.auth.models import Group, User
from rest_framework import serializers

from movies.models import Movie, Genre


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name',read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id",'name']