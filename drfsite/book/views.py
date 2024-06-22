from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import PostSeriaLizer


# class BookAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSeriaLizer # serializers.py

class BookAPIView(APIView):
    def get(self, request):
        lst = Post.objects.all().values()

        return Response({'title': list(lst)})

    def post(self, request):
        post_new = Post.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            genre=request.genre_set['genre'],
            # genre=Genre.genre_set.set(request.data['genre']),
        )
        return Response({'post': model_to_dict(post_new)})
