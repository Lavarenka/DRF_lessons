from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


# class BookModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

# def encode():
#     """
#     переводчит данные в json
#     :return:
#     """
#     model = BookModel('qwead', 'Content:awdawdawd')
#     model_sr = PostSeriaLizer(model) # create dict
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data) # render json
#     print(json)

# def decode():
#     make them a JSON > dict
#     stream = incoming json string
#     data = JSONParser().pars(stream)
#     serializer = PostSeriaLizer(data=data)
#     serializer.is_valid()
