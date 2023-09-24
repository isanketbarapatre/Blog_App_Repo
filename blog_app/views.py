from django.shortcuts import render, redirect
from .models import blogapi
from .serializers import BlogApiSerializers, UserApiSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

# Create your views here.

class BlogListCreateView(ListCreateAPIView):
    queryset = blogapi.objects.all()
    serializer_class = BlogApiSerializers
    permission_classes = [IsAuthenticatedOrReadOnly,]

class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = blogapi.objects.all()
    serializer_class = BlogApiSerializers
    permission_classes = [IsAuthenticatedOrReadOnly,]

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserApiSerializers
    # permission_classes = [IsAuthenticatedOrReadOnly]


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == User.username:
        if password == User.password:
            return Response("User already Created")
        return redirect()
    
    else:
        return Response("User credendials are wrong")
    
