from nfl_calendar import Calendar

# This program aims to tell the user which NFL game from the past week would be the most interesting to watch.
# The link is not yet to nfl.com/stats since I'm still in the process of learning parsing.


def main():

    # We ask the user if he wants to update the html file because too much of it will DDOS the site.
    html_file.update_html()

    # Open the file
    html = html_file.read_html()

    """
    soup = BeautifulSoup(html, "html.parser")

    rows = soup.select('div.game_summaries:nth-child(4)')
    print(rows)
    """


# main()
calendar = Calendar(7)


