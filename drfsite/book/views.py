from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import PostSeriaLizer


class PostViewSet(viewsets.ModelViewSet):
    """
    https://www.django-rest-framework.org/api-guide/viewsets/
    """
    # queryset = Post.objects.all()
    serializer_class = PostSeriaLizer  # serializers.py

    def get_queryset(self):
        """
        фильтры
        queryset должен возвращать лист а не одну запись
        """
        pk = self.kwargs.get('pk')
        if not pk:
            return Post.objects.filter(is_published=True)
        return Post.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def genre(self, request, pk=None):
        """
        добавляем маршрут с категориями через декоратор
        выводим жанры
        :param request:
        :return:
        """
        genres = Genre.objects.get(pk=pk)
        return Response({'genres': genres.title})

# class BookAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSeriaLizer # serializers.py


# class BookApiList(generics.ListCreateAPIView):
#     """
#     ListCreateAPIView // возвращает записи и добавляет записи
#     """
#     queryset = Post.objects.filter(is_published=True)
#     serializer_class = PostSeriaLizer
#
#
# class BookApiUpdate(generics.UpdateAPIView):
#     """
#     нужно выбирать все записи , на самом деле будет выбрана конкретная
#     """
#     queryset = Post.objects.filter(is_published=True)
#     serializer_class = PostSeriaLizer
#
#
# class BookApiCRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.filter(is_published=True)
#     serializer_class = PostSeriaLizer

# class BookAPIView(APIView):
#     """
#     many=True / не конкретная запись а список
#     """
#
#     def get(self, request):
#         """
#         from QuerySet we convert json
#
#         """
#         w = Post.objects.all()
#
#         return Response({'posts': PostSeriaLizer(w, many=True).data})
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSeriaLizer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() # calls the create from method serializer.py
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         """
#         for update
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print(self.request.data)
#         print(1)
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "meth...."})
#
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not ex "})
#
#
#         serializer = PostSeriaLizer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
