from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')), 
    path('api/profiles/', include('prof.urls')),
    path('api/genres/', include('genre.urls')),
    path('api/watchlist', include('watchlist.urls')),
    path('api/programs/', include('program.urls')),
]
