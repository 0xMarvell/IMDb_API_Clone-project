from django.db.models import fields
from rest_framework import serializers
from watchlist.models import WatchList, StreamingPlatform

# Using ModelSerializer
class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'active']
        # exclude = ['active']


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamingPlatform
        fields = '__all__'
        
