from django.urls import path

from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='list'),
    path('<int:pk>/', views.MoviesDetailView.as_view(), name='detail'),
    path('create/', views.MoviesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.MoviesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.MoviesDeleteView.as_view(), name='delete'),
]
