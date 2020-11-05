from pkg_resources import require
from rest_framework import serializers
from snippets.models import Snippet

from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Snippet
        fields = ['id','title','code','linenos','language', 'style', 'owner']
  
    owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'snippets']


