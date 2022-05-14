from django.urls import path

from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.ListProfileWatchlistView.as_view(), name='list-profile-watchlist'),
]
