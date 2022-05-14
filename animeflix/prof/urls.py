from django.urls import path

from prof import views

app_name = 'prof'

urlpatterns = [
    path('', views.ListCreateProfileView.as_view(), name='profile-list-create'),
    path('<int:pk>/', views.DetailProfileView.as_view(), name='profile-detail'),
    path('update/<int:pk>/', views.UpdateProfileView.as_view(), name='profile-update'),
    path('delete/<int:pk>/', views.DeleteProfileView.as_view(), name='profile-delete'),
]
