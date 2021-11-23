from tkinter import *
import webbrowser


def callback(event):
    webbrowser.open_new(event)


class Display:

    def __init__(self, cal):
        """

        :param cal: Calendar object of class calendar
        """
        self.calendar = cal  # Store calendar, used to pull weeks.

        # Creating the root widget, the window.
        self.root = Tk()  # Has to be first, this is the window.
        self.root.title("NFL Stats created by throy45")
        self.root.geometry("650x150")

        # Creating a welcome text.
        self.welcome = Label(self.root, text="Welcome to NFL Stats!")
        self.warning = Label(self.root, fg="red",
                             text="Warning : do not update data frequently.")
        self.warning2 = Label(self.root,
                              text="This could cause an attack on the website.")
        self.instructions = Label(self.root, text="Please select a week.")

        # Drop down box to select week
        self.week_selection = StringVar()
        self.week_selection.set("Select the week")
        self.weeks = ["Week " + str(1 + i) for i in range(18)]
        self.week_dropdown = OptionMenu(self.root, self.week_selection,
                                        *self.weeks)

        # Entry fields to specify the weightings by element
        self.int_prompt = Label(self.root, text="Enter interception weight :")
        self.ot_prompt = Label(self.root, text="Enter overtime weight :")
        self.mfg_prompt = Label(self.root, text="Enter missed field goal "
                                                "weight :")
        self.int_input = Entry(self.root, width=25)
        self.ot_input = Entry(self.root, width=25)
        self.mfg_input = Entry(self.root, width=25)

        interception, overtime, missed_fg = 0, 0, 0
        self.parameters = [interception, overtime, missed_fg]
        self.all_input = [self.int_input, self.ot_input, self.mfg_input]

        # Creating buttons. Usually don't put parenthesis in command's function
        # but here click is returning a function
        self.all_submit = Button(self.root, text="Save all", cursor="hand2",
                                 command=self.click_all)
        self.get_games_button = Button(self.root, command=self.get_games,
                                       cursor="hand2", text="See games of "
                                                            "corresponding week")
        self.update_data = Button(self.root, text="Update data", cursor="hand2",
                                  command=self.calendar.update_all_html,
                                  fg="red")

    def get_game_link(self, week_nb, game):
        """

        :param week_nb:
        :param game:
        :return:
        """
        self.calendar.games[week_nb][game][2]
        self.link[game] = Label(self.root, text="Game 1", fg="blue",
                                cursor="hand2")
        self.link[game].bind("<Button-1>", lambda e: webbrowser.open_new(
                "https://www.pro-football-reference.com/boxscores/202109090tam.htm"))

    def save_entry(self, index):
        """
        Gets the value that the user put in the Entry field of corresponding
        index. Stores in self.parameters by corresponding index.
        :param index: Given to specify which element to fetch and store.
        :return:
        """
        self.parameters[index] = int(self.all_input[index].get())

    def click_all(self):
        """
        Cycles on save_entry method to get all the values that the user has
        input in the Entry fields. Save_entry stores them.
        :return:
        """
        for index in range(len(self.all_input)):
            self.save_entry(index)

    def create_grid(self):
        """
        Creates the disposition grid for the widgets
        :return:
        """
        self.welcome.grid(row=0, column=1)
        self.warning.grid(row=1, column=0)
        self.warning2.grid(row=1, column=1)
        self.update_data.grid(row=1, column=2)
        self.int_prompt.grid(row=2, column=0)
        self.int_input.grid(row=2, column=1)
        self.ot_prompt.grid(row=3, column=0)
        self.ot_input.grid(row=3, column=1)
        self.mfg_prompt.grid(row=4, column=0)
        self.mfg_input.grid(row=4, column=1)
        #self.all_submit.grid(row=4, column=2) # doesnt work atm
        self.week_dropdown.grid(row=5, column=1)
        self.instructions.grid(row=5, column=0)
        self.get_games_button.grid(row=5, column=2)

    def get_week_selection(self):
        """
        Returns the week selected in the drop-down menu.
        :return: str of syntax "Week 1"
        """
        return self.week_selection.get()

    def get_weighting(self):
        """
        Returns the parameters weightings to suggest games.
        :return:
        """
        return self.parameters

    def get_games(self):
        """
        Gets the games following selection in drop-down menu.
        :return:
        """
        window = Toplevel(self.root)
        week = self.get_week_selection()
        week_selection = Label(window, text=week)
        week_selection.pack()

        week_nb = int(week[5:])
        try:
            self.calendar.update_week_games(week_nb)
            for game in self.calendar.games[week_nb].keys():
                text = Label(window, text=game + " : "
                                          + self.calendar.games[week_nb][game][1])
                text.pack()

                link = Label(window, text="stats link", fg="blue", cursor="hand2")
                link.pack()
                link.bind("<Button-1>", lambda e: callback(self.calendar.games[
                                                               week_nb][game][2]))
        except ValueError:
            no_games = Label(window, text="No games in selected week, " +
                                          "try updating.")
            no_games.pack()

    def run(self):
        """
        Main function to run the GUI. Creates grid, then runs mainloop.
        :return:
        """
        self.create_grid()

        # Main loop for the GUI.
        self.root.mainloop()
