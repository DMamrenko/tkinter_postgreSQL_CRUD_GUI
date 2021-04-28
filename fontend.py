"""
A CRUD program for records of employees.
"""
from tkinter import *

# Creating the Window
window = Tk()
window.geometry('575x380')
window.title('Employee CRUD')

# Labels
PADX, PADY = 15, 8
employeeCRUDLabel = Label(window, text='Employee CRUD', pady=10)
fnameLabel = Label(window, text='First Name:', padx=PADX, pady=PADY)
lnameLabel = Label(window, text='Last Name:', padx=PADX, pady=PADY)
positionLabel = Label(window, text='Position:', padx=PADX, pady=PADY)
idLabel = Label(window, text='ID:', padx=PADX, pady=PADY)
resultsLabel = Label(window, text='Results:')

# Entries
ENTRYWIDTH = 35
fnameEntry = Entry(window, width=ENTRYWIDTH)
lnameEntry = Entry(window, width=ENTRYWIDTH)
positionEntry = Entry(window, width=ENTRYWIDTH)
idEntry = Entry(window, width=ENTRYWIDTH)

# Buttons
BUTTONWIDTH = 10
searchButton = Button(window, text='Search', width=BUTTONWIDTH)
createButton = Button(window, text='Create', width=BUTTONWIDTH)
updateButton = Button(window, text='Update', width=BUTTONWIDTH)
deleteButton = Button(window, text='Delete', width=BUTTONWIDTH)
viewAllButton = Button(window, text='View All', width=BUTTONWIDTH)

# Listbox and Scrollbar
LISTBOXWIDTH = 60
listboxFrame = Frame(window)
resultsScrollbar = Scrollbar(listboxFrame)
resultsListbox = Listbox(listboxFrame, width=LISTBOXWIDTH, yscrollcommand=resultsScrollbar)
resultsScrollbar.config(command = resultsListbox.yview)
resultsListbox.pack(side=LEFT, fill=X)
resultsScrollbar.pack(side=RIGHT, fill=Y)

    # Insert elements into the listbox
for values in range(100):
    resultsListbox.insert(END, values)

# Placing Widgets
    # Labels
employeeCRUDLabel.grid(row=0, column=1)
fnameLabel.grid(row=1, column=0, sticky=E)
lnameLabel.grid(row=2, column=0, sticky=E)
positionLabel.grid(row=3, column=0, sticky=E)
idLabel.grid(row=4, column=0, sticky=E)
resultsLabel.grid(row=5, column=1)

    # Entries and associated StringVars
fnameEntry.grid(row=1, column=1)
lnameEntry.grid(row=2, column=1)
positionEntry.grid(row=3, column=1)
idEntry.grid(row=4, column=1)
fnameText = StringVar()
lnameText = StringVar()
positionText = StringVar()
idText = StringVar()

    # Buttons
searchButton.grid(row=1, column=2)
createButton.grid(row=2, column=2)
updateButton.grid(row=3, column=2)
deleteButton.grid(row=4, column=2)
viewAllButton.grid(row=6, column=0, sticky=N)

    # Listbox and Scrollbar
listboxFrame.grid(row=6, column=1, columnspan=2)

# Keeping the application running until close
window.mainloop()