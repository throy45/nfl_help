from tkinter import *

# Creating the root widget, the window.
root = Tk()  # Has to be first, this is the window.
root.title("NFL Stats created by throy45")
root.geometry("400x400")

# Creating a welcome text.
welcome = Label(root, text="Welcome to NFL Stats.")
instructions = Label(root, text="Please select a week.")

# Drop down box to select week
week_selection = StringVar()
week_selection.set("Select the week")
weeks = ["Week " + str(i) for i in range(18)]
week_dropdown = OptionMenu(root, week_selection, *weeks)

interception, overtime, missed_fg = 0, 0, 0
parameters = [interception, overtime, missed_fg]

int_prompt = Label(root, text="Enter interception weight :")
ot_prompt = Label(root, text="Enter overtime weight :")
mfg_prompt = Label(root, text="Enter missed field goal weight :")

int_input = Entry(root, width=25)
ot_input = Entry(root, width=25)
mfg_input = Entry(root, width=25)


# clicking function
def click(element, index):
    parameters[index] = element.get()


# Creating buttons. Usually don't put parenthesis in command's function
# but here click is returning a function
int_submit = Button(root, text="Save", command=click(int_input, 0))
ot_submit = Button(root, text="Save", command=click(ot_input, 1))
mfg_submit = Button(root, text="Save", command=click(mfg_input, 2))

# Disposition of widgets
welcome.grid(row=0, column=1)
instructions.grid(row=1, column=1)
int_prompt.grid(row=2, column=0)
int_input.grid(row=2, column=1)
int_submit.grid(row=2, column=2)
ot_prompt.grid(row=3, column=0)
ot_input.grid(row=3, column=1)
ot_submit.grid(row=3, column=2)
mfg_prompt.grid(row=4, column=0)
mfg_input.grid(row=4, column=1)
mfg_submit.grid(row=4, column=2)
week_dropdown.grid(row=5, column=1)

# Main loop for the GUI.
root.mainloop()

print(parameters)
