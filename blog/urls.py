from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostRetrieveView,
    PostUpdateView,
    PostDestroyView,
    PostListHomeView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post_home/', PostListHomeView.as_view(), name='post-list-home'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostRetrieveView.as_view(), name='post-retrieve'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDestroyView.as_view(), name='post-delete'),
]
