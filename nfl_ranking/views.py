from django.shortcuts import render
from django.db import models
from .models import NFLGame, Turnover


def game_ranking(request):
    # Fetch data, rank games by turnovers, and pass them to the template
    games_with_turnovers = NFLGame.objects.filter(turnover__isnull=False).annotate(
        num_turnovers=models.Count('turnover')).order_by('-num_turnovers')
    context = {'games_with_turnovers': games_with_turnovers}
    return render(request, 'nfl_ranking/game_ranking.html', context)
