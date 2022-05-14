from django.urls import path

from genre import views

app_name = 'genre'

urlpatterns = [
    path('', views.ListGenreIDsView.as_view(), name='genres'),
]
