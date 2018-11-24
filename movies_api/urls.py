from django.urls import path
from .views import Movies, Movie_detail

urlpatterns = [
    path('', Movies.as_view()),
    path('<int:id>/', Movie_detail.as_view()),
]





