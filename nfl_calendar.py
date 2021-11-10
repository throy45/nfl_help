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
        Creates two dictionaries, self.weeks and self.games.
        self.weeks : Stores each html week file
        self.games : Stores date and teams for each games in a 2D dict.
                     structure : self.games[week_number][game_name] =
                                                (datetime.date, Team1Team2 str,
                                                 gamehyperlink str)

        :param current_week: int
        """
        self.current_week = current_week
        self.weeks = {}
        self.games = {}
        for index in range(18):
            week_nb = index + 1
            self.load_week_html(week_nb)
            self.games[week_nb] = {}
            if week_nb < self.current_week:
                self.update_week_games(week_nb)

        # Add games to self.games dict (so add the date and the teams. since
        # we don't have the info for the current week we need to do until
        # last week.

    def get_html(self, week_nb):
        """
        Returns an HTML class object, read from a file in the current directory.
        :param week_nb: int
        :return: HTML object
        """
        file_name = "week_" + str(week_nb)
        return HTML(file_name)

    def load_week_html(self, week_nb):
        """
        Loads/reloads the specified week into the self.weeks dict.
        :param week_nb:
        :return:
        """
        week_html = self.get_html(week_nb)
        self.weeks[week_nb] = week_html.read_html()

    def update_week_html(self, week_nb):
        """
        Retrieves the games happening on week week_nb and creates/updates the
        html file. Then updates the corresponding item in the self.weeks dict.
        Then updates the corresponding games in the self.games dict.
        :param week_nb: integer (between 1 and 18)
        :return: none
        """
        week_html = self.get_html(week_nb)
        week_html.update_html(week_nb, bypass=True)
        self.weeks[week_nb] = week_html.read_html()
        if week_nb < self.current_week:
            self.update_week_games(week_nb)

    def update_all_html(self):
        """
        Updates weeks html files.
        :return: None
        """
        for i in range(self.current_week):
            self.update_week_html(i + 1)

    def update_week_games(self, week_nb):
        """
        Adds or updates the games for specified week in the games dict.
        Currently can only fetch past games.
        :param week_nb: int
        :return:
        """

        # Creates HTML instance to be able to retrieve it with read_html method
        week_html = self.get_html(week_nb)
        html = week_html.read_html()

        # uses Beautiful Soup to parse the html and find the section
        # corresponding to the match
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select('.game_summary')

        self.create_all_games_in_week(week_nb, rows)

    def create_all_games_in_week(self, week_nb, html_rows):
        """
        for every game (16) per week, create an element for that game in
        # self.games
        :param week_nb: int
        :param html_rows: beautiful soup html element
        :return: none
        """

        for game_index in range(16):
            try:
                game_name = f"Game {str(game_index + 1)}"

                # select the date of the particular game
                date = html_rows[game_index].select_one('.date td').text.strip()
                # convert it to datetime.date element to be able to compare with
                # today's date
                date = datetime.datetime.strptime(date, "%b %d, %Y").date()

                # select the winner's and the loser's name
                loser = html_rows[game_index].select_one('.loser td').text.strip()
                winner = html_rows[game_index].select_one('.winner td').text.strip()

                # select the game link using some string formatting
                # unfortunately my limited knowledge of html and css falls short here so
                # I resorted to this method.
                link = html_rows[game_index].select_one('.gamelink').find_all('a',
                href=True)
                link = str(link)[10:37]
                link = "https://www.pro-football-reference.com/" + link

                # we flip a coin to be unable to tell who won and who lost.
                # (because we don't want to spoil the user)
                # and then we store the date, teams and the link.
                if random.random() > .5:
                    self.games[week_nb][game_name] = (date, f"{loser} & {winner}", link)
                else:
                    self.games[week_nb][game_name] = (date, f"{winner} & {loser}", link)

            except IndexError:
                print("Index error. Week " +  str(week_nb) +
                      " doesn't seem to have 16 games. Continuing.")
                continue
            except ValueError:
                print("Value error. Continuing.")
                continue


"""
teams = ["crd", "atl", "rav", "buf", "car", "chi", "cin", "cle",
                      "dal", "den", "det", "gnb", "htx", "clt", "jax", "kan",
                      "rai", "sdg", "ram", "mia", "min", "nwe", "nor", "nyg",
                      "nyj", "phi", "pit", "sfo", "sea", "tam", "oti", "was"]
"""