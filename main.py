from nfl_calendar import Calendar
from GUI import Display

# First this programs gives the users the NFL games from the week he selects.
# Then it aims to tell the user which NFL game from the past week would
# be the most interesting to watch (not yet achieved).


def main():
    calendar = Calendar(9)

    dis = Display(calendar)
    dis.run()



main()


