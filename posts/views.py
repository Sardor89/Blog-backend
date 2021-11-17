from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorReadOnly
# Create your views here.


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer





