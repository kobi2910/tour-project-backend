from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('api/blog/', include('blog.urls')), 
    path('api/news/', include('news.urls')),
    path('api/guides/', include('user_accounts.urls')),
    path('api/account/', include('user_accounts.urls')),   
    path('api/trips/', include('trip.urls')),
    path('api/contact_us/', include('contact_us.urls')),
    path('admin/', admin.site.urls),
]
