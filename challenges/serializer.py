from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing for our api view"""
    name=serializers.CharField(max_length=10)
    