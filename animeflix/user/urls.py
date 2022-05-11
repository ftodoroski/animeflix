from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view() , name='logout'),
    path('delete-account/<int:pk>', views.DeleteUserView.as_view(), name='delete-account'),
    path('update/<int:pk>', views.UpdateUserView.as_view() , name='update'),
]
