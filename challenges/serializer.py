from unittest.util import _MAX_LENGTH
from rest_framework import serializers
#from challenges import models
from . import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing for our api view"""
    name=serializers.CharField(max_length=10)
    # email=serializers.CharField(max_length=100)
    # number=serializers.

class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object """

    class Meta :
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True
                ,'style':{ 'input_type':'password' }
            }
        }

    def create(self,validated_data):
      """create a new user"""
      user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password'],
      )
      return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text')
        extra_kwargs = {'user_profile': {'read_only': True}}