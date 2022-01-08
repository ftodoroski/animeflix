from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token-auth/', views.CreateTokenView.as_view(), name='token_auth'),
    path('me/', views.ManageUserView.as_view(), name='me')
]