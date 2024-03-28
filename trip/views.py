from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from proj_home.permissions import IsOwnerOrAdminPermission, IsGuidePermission
from .models import Trip
from .serializers import TripSerializer
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


class TripListView(generics.ListAPIView):
    """
    View to retrieve a list of all trips.

    Endpoint: /trips/
    Method: GET
    Permissions: AllowAny
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Get the queryset for the list of trips.

        Returns:
            queryset (QuerySet): List of all trips.
        """
        queryset = super().get_queryset()
        return queryset

class TripListHomeView(generics.ListAPIView):
    """
    View to retrieve a list of the newest 5 trips for the home page.

    Endpoint: /trips/home/
    Method: GET
    Permissions: AllowAny
    """
    serializer_class = TripSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Get the queryset for the list of newest trips for the home page.

        Returns:
            queryset (QuerySet): List of the newest 5 trips.
        """
        return Trip.objects.all().order_by('-created_at')[:5]

class TripDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific trip.

    Endpoint: /trips/{id}/
    Method: GET
    Permissions: AllowAny
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [AllowAny]

class TripCreateView(generics.CreateAPIView):
    """
    View to create a new trip.

    Endpoint: /trips/create/
    Method: POST
    Permissions: IsAuthenticated, IsGuidePermission
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated, IsGuidePermission]

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to create a new trip.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            response (HttpResponse): The HTTP response object.
        """
        print("Request data:", request.data)  # Print the request data
        print("User:", request.user)  # Print the user making the request
        print("Method:", request.method)  # Print the HTTP method used
        print("Headers:", request.headers)  # Print the request headers
        print("Content Type:", request.content_type)  # Print the request content type
        print("User Agent:", request.headers.get('User-Agent'))  # Print the user agent

        # Call the parent class post method to continue with the default behavior
        return super().post(request, *args, **kwargs)

class TripUpdateView(generics.UpdateAPIView):
    """
    View to update an existing trip.

    Endpoint: /trips/{id}/update/
    Method: PUT/PATCH
    Permissions: IsAuthenticated, IsOwnerOrAdminPermission
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminPermission]

class TripDeleteView(generics.DestroyAPIView):
    """
    View to delete an existing trip.

    Endpoint: /trips/{id}/delete/
    Method: DELETE
    Permissions: IsAuthenticated, IsOwnerOrAdminPermission
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminPermission]
