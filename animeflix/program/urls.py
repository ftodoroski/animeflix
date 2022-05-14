from django.urls import path

from program import views

app_name = 'program'

urlpatterns = [
    path('', views.ListGenreProgramView.as_view(), name='genre-based-program-list'),
    path('<int:pk>/', views.DetailProgramViews.as_view(), name='program-detail')
]
