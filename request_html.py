import requests


class HTML:
    """
    This class handles all things HTML.
    (fetching html, saving to file, reading file, updating the instance's file)
    """

    def __init__(self, file_name):
        """
        Initializes the html instance
        :param file_name: str name to give html file. .html will be added
        """
        self.name = file_name + ".html"

    def save_html(self, html):
        """
        Takes new html data and stores it within the file linked with that instance.
        :param html: html data
        :return: none
        """""
        with open(self.name, 'wb') as file:
            file.write(html)

    def read_html(self):
        """
        Return html data stored in the instance's file
        :return: html data
        """
        try:
            with open(self.name, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found. Returning none.")
            return None

    def update_html(self, week_nb, *, bypass=False):
        """
        Prompts the user if he (really) wants to update the html file stored.
        If so, will update according to self.url and save with save_html
        :param week_nb: week number used to define url
        :param bypass: bypass the warning about ddos
        :return: none
        """

        if bypass:
            update_html = "True"
        else:
            print(f"Do you want to update \"{self.name}\"?")
            print("Doing so too often might trigger DDOS.")
            while True:
                update_html = input(f"Update \"{self.name}\"? (True or False): ")
                if update_html not in ("True", "False"):
                    print("Wrong value, try again.")
                else:
                    break

        if update_html == "True":
            url = "https://www.pro-football-reference.com/years/2021/week_" + \
                   str(week_nb) + ".htm"
            r = requests.get(url)
            self.save_html(r.content)
            print("Html file updated successfully.")
