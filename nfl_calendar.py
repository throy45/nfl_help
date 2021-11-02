from request_html import HTML
from bs4 import BeautifulSoup
import random
import datetime


class Calendar:
    """
    Class used to get games happening every week.
    """

    def __init__(self, current_week):
        """
        Creates two dictionnaries, self.weeks and self.games.
        self.weeks : Stores each html week file
        self.games : Stores date and teams for each games in a 2D dict.
                     structure : self.games[week_number][game_name]

        :param current_week: int
        """
        self.current_week = current_week
        self.weeks = {}
        self.games = {}
        for week_index in range(18):
            week_nb = week_index + 1
            url = "https://www.pro-football-reference.com/years/2021/week_" + \
                  str(week_nb) + ".htm"
            file_name = "week_" + str(week_nb)
            week_html = HTML(url, file_name)
            self.weeks[week_nb] = week_html.read_html()
            self.games[week_nb] = {}

        # Add games to self.games dict (so add the date and the teams. since
        # we don't have the info for the current week we need to do until
        # last week.
        for week_index in range(current_week - 1):
            self.update_week_games(week_index + 1)

    def update_week_file(self, week_nb):
        """
        Retrieves the games happening on week week_nb and creates/updates the
        html file.
        :param week_nb: integer (between 1 and 18)
        :return:
        """
        week_nb = str(week_nb)
        url = "https://www.pro-football-reference.com/years/2021/week_" + \
              week_nb + ".htm"
        file_name = "week_" + week_nb

        html_file = HTML(url, file_name)

        html_file.update_html(bypass=True)

    def update_all_weeks_files(self, *, bypass=False, ):
        """
        Updates ALL 18 weeks html files. Requires bypass because 18 requests.
        :param bypass: boolean
        :return: None
        """
        if bypass:
            for i in range(18):
                self.update_week_file(i + 1)

    def update_week_games(self, week_nb):  # ######## ici
        """
        Adds or updates the games for specified week in the games dict.
        Currently can only fetch past games.
        :param week_nb: int
        :return:
        """
        url = "https://www.pro-football-reference.com/years/2021/week_" + str(
                week_nb) + ".htm"
        file_name = "week_" + str(week_nb)

        # Creates HTML instance to be able to retrieve it with read_html method
        html_file = HTML(url, file_name)
        html = html_file.read_html()

        # uses Beautiful Soup to parse the html and find the section
        # corresponding to the match
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select('.game_summary')

        # for every game (16) per week, create an element for that game in
        # self.games
        for game_index in range(16):
            game_name = f"Game {str(game_index + 1)}"

            # select the date of the particular game
            date = rows[game_index].select_one('.date td').text.strip()
            # convert it to datetime.date element to be able to compare with
            # today's date
            date = datetime.datetime.strptime(date, "%b %d, %Y").date()

            # select the winner's and the loser's name
            loser = rows[game_index].select_one('.loser td').text.strip()
            winner = rows[game_index].select_one('.winner td').text.strip()

            # we flip a coin to be unable to tell who won and who lost.
            # (because we don't want to spoil the user)
            if random.random() > .5:
                self.games[week_nb][game_name] = (date, f"{loser} & {winner}")
            else:
                self.games[week_nb][game_name] = (date, f"{winner} & {loser}")

    def generate_link(self, week_nb):
        """
        Generate the url for the specified week_nb
        :param week_nb:
        :return:
        """
