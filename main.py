from nfl_calendar import Calendar
from GUI import Display

# This program aims to tell the user which NFL game from the past week would be the most interesting to watch.
# The link is not yet to nfl.com/stats since I'm still in the process of learning parsing.


def main():
    calendar = Calendar(6)

    dis = Display(calendar)
    dis.run()



main()


