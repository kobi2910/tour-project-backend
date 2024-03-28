from rest_framework import generics
from rest_framework import authentication
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from proj_home.permissions import IsOwnerOrAdminPermission, IsGuidePermission
from django.utils import timezone

class PostListView(generics.ListAPIView):
    """
    View to retrieve a list of all posts.

    This view allows any user to retrieve a list of all posts in the database.

    Endpoint: /posts/
    HTTP Methods: GET
    """
    queryset = Post.objects.all().order_by('date')
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostListHomeView(generics.ListAPIView):
    """
    View to retrieve a list of recent posts.

    This view allows any user to retrieve a list of the two most recent posts in the database.

    Endpoint: /posts/home/
    HTTP Methods: GET
    """
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.all().order_by('date')[:2]


class PostRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a single post.

    This view allows any user to retrieve a single post by its ID.

    Endpoint: /posts/{id}/
    HTTP Methods: GET
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostCreateView(generics.CreateAPIView):
    """
    View to create a new post.

    This view allows authenticated users with guide permissions to create a new post.

    Endpoint: /posts/create/
    HTTP Methods: POST
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsGuidePermission] 


class PostUpdateView(generics.UpdateAPIView):
    """
    View to update an existing post.

    This view allows the owner or an admin user to update an existing post.

    Endpoint: /posts/{id}/update/
    HTTP Methods: PUT, PATCH
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdminPermission]
    
    def perform_update(self, serializer):
        print(self.request.data)
        serializer.save(author=self.request.user, date=timezone.now())


class PostDestroyView(generics.DestroyAPIView):
    """
    View to delete an existing post.

    This view allows the owner or an admin user to delete an existing post.

    Endpoint: /posts/{id}/delete/
    HTTP Methods: DELETE
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdminPermission]
    


    