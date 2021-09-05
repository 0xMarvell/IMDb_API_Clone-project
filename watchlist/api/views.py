from django.shortcuts import render
from rest_framework import response, serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist.models import WatchList, StreamingPlatform
# Create your views here.

# USING CLASS-BASED VIEWS

class StreamingPlatform(APIView):

    def get(self, request):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamingPlatformDetail(APIView):

    def get(self, request, pk):  
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({"Error":"Streaming platform does not exist :( :("}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        StreamingPlatform.delete()
        return Response({'Confirmation':'Operation Successful'}, status=status.HTTP_204_NO_CONTENT)


class WatchList(APIView):

    def get(self, request):
        shows = WatchList.objects.all()
        serializer = WatchListSerializer(shows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetail(APIView):

    def get(self, request, pk):
        try:
            show = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie Does Not Exist :( :('}, status=status.HTTP_400_BAD_REQUEST)
        serializer = WatchListSerializer(show)
        return Response(serializer.data)

    def put(self, request, pk):
        show = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(show, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show = WatchList.objects.get(pk=pk)
        WatchList.delete()
        return Response({'Confirmation':'Operation Successful'}, status=status.HTTP_204_NO_CONTENT)




