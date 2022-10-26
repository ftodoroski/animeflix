from django.urls import path

from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.ProfileWatchlistView.as_view(), name='list-profile-watchlist'),
    path('/create', views.ProfileWatchlistView.as_view(), name='add-program-watchlist'),
    path('/delete/<int:pk>', views.ProfileWatchlistView.as_view(), name='delete-program-watchlist')
]
