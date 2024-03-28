from django.urls import path
from .views import MsgCreateView



urlpatterns = [
    path('new_msg/', MsgCreateView.as_view(), name='contact-us'),
]
