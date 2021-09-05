from django.urls import path
from watchlist.api.views import MovieList, MovieDetail, StreamingPlatform, StreamingPlatformDetail

urlpatterns = [
    path('watchlist', MovieList.as_view(), name='watchlist'),
    path('watchlist/<int:pk>', MovieDetail.as_view(), name='watchlist-detail'),
    path('streaming-platform', StreamingPlatform.as_view(), name='streaming-platform'),
    path('streaming-platform/<int:pk>', StreamingPlatformDetail.as_view(), name='streamingplatform-detail'),
]