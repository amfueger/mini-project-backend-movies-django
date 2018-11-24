from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies_api.urls')),
    path('users/', include('accounts_api.urls')),
]

# CHECKED - Matches Jim's code
