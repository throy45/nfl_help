from django.db import models


class NFLGame(models.Model):
    game_id = models.CharField(max_length=20)
    week = models.IntegerField()
    home_team = models.CharField(max_length=3)
    away_team = models.CharField(max_length=3)

    def __str__(self):
        return self.game_id  # Return the game_id as the string representation


class Turnover(models.Model):
    game = models.ForeignKey(NFLGame, on_delete=models.CASCADE)
    turnover_type = models.CharField(max_length=20)

    def __str__(self):
        return self.turnover_type  # Return the turnover_type as the string representation
