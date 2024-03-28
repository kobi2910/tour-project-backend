from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAdminUser


class NewsListView(generics.ListAPIView):
    """
    View to retrieve a list of news articles.

    Endpoint: /news/
    Method: GET
    """
    queryset = News.objects.all().order_by('date')
    serializer_class = NewsSerializer
    permission_classes = []

class NewsCreateView(generics.CreateAPIView):
    """
    View to create a new news article.

    Endpoint: /news/create/
    Method: POST
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

class NewsRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a specific news article.

    Endpoint: /news/<int:pk>/
    Method: GET
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = []

class NewsUpdateView(generics.UpdateAPIView):
    """
    View to update a specific news article.

    Endpoint: /news/<int:pk>/update/
    Method: PUT/PATCH
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

class NewsDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific news article.

    Endpoint: /news/<int:pk>/delete/
    Method: DELETE
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]
