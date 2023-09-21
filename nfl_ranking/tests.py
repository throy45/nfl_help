from django.test import TestCase
from django.urls import reverse
from .models import NFLGame, Turnover


class NFLGameModelTest(TestCase):
    def test_create_nfl_game(self):
        game = NFLGame.objects.create(
            game_id='2023_01_ARI_WAS',
            week=1,
            home_team='ARI',
            away_team='WAS',
            # Add more fields as needed
        )
        # Customize the __str__ method as needed
        self.assertEqual(game.__str__(), '2023_01_ARI_WAS')

    def test_nfl_game_week(self):
        game = NFLGame.objects.create(
            game_id='2023_02_CLE_PIT',
            week=2,
            home_team='CLE',
            away_team='PIT',
            # Add more fields as needed
        )
        self.assertEqual(game.week, 2)


class TurnoverModelTest(TestCase):
    def setUp(self):
        self.game = NFLGame.objects.create(
            game_id='2023_01_ARI_WAS',
            week=1,
            home_team='ARI',
            away_team='WAS',
            # Add more fields as needed
        )

    def test_create_turnover(self):
        turnover = Turnover.objects.create(
            game=self.game,
            turnover_type='Interception',
            # Add more fields as needed
        )
        # Customize the __str__ method as needed
        self.assertEqual(turnover.__str__(), 'Interception')

    def test_turnover_game_relationship(self):
        turnover = Turnover.objects.create(
            game=self.game,
            turnover_type='Fumble',
            # Add more fields as needed
        )
        self.assertEqual(turnover.game, self.game)


class GameRankingViewTest(TestCase):
    def setUp(self):
        # Create test data for NFL games and turnovers
        self.game1 = NFLGame.objects.create(
            game_id='2023_01_ARI_WAS', week=1, home_team='ARI', away_team='WAS')
        self.game2 = NFLGame.objects.create(
            game_id='2023_02_CLE_PIT', week=2, home_team='CLE', away_team='PIT')
        Turnover.objects.create(game=self.game1, turnover_type='Interception')
        Turnover.objects.create(game=self.game1, turnover_type='Fumble')
        Turnover.objects.create(game=self.game2, turnover_type='Interception')

    def test_game_ranking_view(self):
        # Test the game ranking view
        url = reverse('game_ranking')  # Get the URL for the view
        response = self.client.get(url)  # Make a GET request to the view
        # Check if the response is successful (HTTP 200)
        self.assertEqual(response.status_code, 200)
        # Check if game data is present in the response
        self.assertContains(response, '2023_01_ARI_WAS')
        self.assertContains(response, '2023_02_CLE_PIT')
        # Check if turnovers are present
        self.assertContains(response, 'Interception')

    def test_game_ranking_template(self):
        # Test rendering of the game ranking template
        url = reverse('game_ranking')
        response = self.client.get(url)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'nfl_ranking/game_ranking.html')

    def test_game_ranking_template_context(self):
        # Test template context data
        url = reverse('game_ranking')
        response = self.client.get(url)
        # Check if 'games_with_turnovers' is in the context
        self.assertIn('games_with_turnovers', response.context)
