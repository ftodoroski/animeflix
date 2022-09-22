from django.urls import path

from program import views

app_name = 'program'

urlpatterns = [
    path('', views.ListProgramView.as_view(), name='program-list'),
    path('<int:pk>', views.DetailProgramViews.as_view(), name='program-detail')
]