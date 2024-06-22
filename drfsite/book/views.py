from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import PostSeriaLizer


class BookAPIView(generics.ListAPIView):
    """

    """

    queryset = Post.objects.all()
    serializer_class = PostSeriaLizer # serializers.py
