from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import change_password,register_user, guide_list, check_token, get_user_from_token,serve_guide_detail


urlpatterns = [
    path('check_token/', check_token, name='check_token'),
    path('get_user/', get_user_from_token, name='get_user'),
    path('register/', register_user, name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_complete/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
 
    path('change_password/', change_password, name='change_password'),

    path('guides/', guide_list, name='guides'),
    path('guides/<int:pk>/', serve_guide_detail, name='guide_detail')
    
]



