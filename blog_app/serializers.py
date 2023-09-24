from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token  

class BlogApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = blogapi
        fields =  ('id', 'title', 'content', 'publication_date')

class UserApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_user):
        user = User.objects.create(
            username=validated_user['username'],
            password=validated_user['password'] 
        )
        Token.objects.create(user=user)
        return user