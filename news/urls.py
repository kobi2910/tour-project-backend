
from django.urls import path
from .views import (
    NewsListView,
    NewsCreateView,
    NewsRetrieveView,
    NewsUpdateView,
    NewsDestroyView,
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('create/', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/', NewsRetrieveView.as_view(), name='news-retrieve'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name='news-update'),
    path('delete/<int:pk>/', NewsDestroyView.as_view(), name='news-delete'),
]
