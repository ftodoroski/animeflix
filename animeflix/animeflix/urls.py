from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')), 
    path('api/programs/', include('program.urls')),
    path('api/profiles/', include('prof.urls'))
]
