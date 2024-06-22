from rest_framework import serializers

from .models import *




class PostSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'genre',)
