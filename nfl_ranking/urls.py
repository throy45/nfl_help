from django.urls import path
from . import views

urlpatterns = [
    path('game-ranking/', views.game_ranking, name='game_ranking'),
    # Add more URL patterns for other views as needed
]
