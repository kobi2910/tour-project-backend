from django.urls import path
from .views import TripListView, TripDetailView,TripCreateView,TripUpdateView,TripDeleteView, TripListHomeView


urlpatterns = [
    path('', TripListView.as_view(), name='trip-list'),
    path('trips_home/', TripListHomeView.as_view(), name='trip-list-home'),
    path('create/', TripCreateView.as_view(), name='trip-create'),
    path('<int:pk>/update/', TripUpdateView.as_view(), name='trip-update'),
    path('delete', TripDeleteView.as_view(), name='trip-delete'),
    path('<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
]
