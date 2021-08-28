from django.shortcuts import render

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie
# Create your views here.

# USING FUNCTION-BASED VIEWS

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie Does Not Exist :( :('}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk = pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk = pk)
#         movie.delete()
#         return Response({'Confirmation':'Operation Successful'}, status=status.HTTP_204_NO_CONTENT)

# USING CLASS-BASED VIEWS

class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Does Not Exist :( :('}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'Confirmation':'Operation Successful'}, status=status.HTTP_204_NO_CONTENT)