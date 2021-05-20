"""
A CRUD program for records of employees.
"""
from tkinter import *
import tkinter.font as font
import backend
import formatter
import validator

# Button Functionality
def clearResultsListbox():
    resultsListbox.delete(0, END)

def clearFields():
    fnameEntry.delete(0, END)
    lnameEntry.delete(0, END)
    positionEntry.delete(0, END)
    idEntry.delete(0, END)

def updateStatusText(text):
    statusText.delete(1.0, END)
    statusText.insert(1.0, text)

def clearStatusText():
    updateStatusText('')

def getSelectedRow(event):
    try:
        global selectedRow
        i = resultsListbox.curselection()[0]
        selectedRow = resultsListbox.get(i)
        populateFieldsFromSelectedRow()
    except IndexError:
        pass

def onMouseWheel(event):
    resultsListbox.yview_scroll(int(-1 * (event.delta/120)), UNITS)

def populateFieldsFromSelectedRow():
    clearFields()
    iden, fname, lname, position = formatter.reverseFormat(selectedRow)
    fnameEntry.insert(0, fname)
    lnameEntry.insert(0, lname)
    positionEntry.insert(0, position)
    idEntry.insert(0, iden)

def viewAllCommand():
    clearResultsListbox()
    rows = backend.viewAll()
    allRows = formatter.formatResults(rows)
    for row in allRows:
        resultsListbox.insert(END, row)
    clearFields()
    updateStatusText(f'Showing {len(rows)} results.')

def hideAllCommand():
    clearResultsListbox()
    clearFields()
    updateStatusText(f'Hiding all results.')

def searchByEnter(event):
    searchCommand()

def searchCommand():
    clearResultsListbox()
        # If this is a strict search, use backend.strictSearch(), otherwise, use backend.looseSearch()
    doingStrictSearch = strictValue.get() == 1
    if doingStrictSearch:
        rows = backend.strictSearch(idText.get(), fnameText.get(), lnameText.get(), positionText.get())
        searchResults = formatter.formatResults(rows)
    else:
        rows = backend.looseSearch(idText.get(), fnameText.get(), lnameText.get(), positionText.get())
        searchResults = formatter.formatResults(rows)

    for row in searchResults:
        resultsListbox.insert(END, row)
    
    # Changing status depending on how many results found.
    if len(rows) == 0:
        updateStatusText('No results found.')
    elif len(rows) == 1:
        updateStatusText('1 result found.')
    else:
        updateStatusText(f'{len(rows)} results found.')

def insertCommand():
    fname, lname, position = fnameText.get(), lnameText.get(), positionText.get()
    if validator.validateInsertion(fname, lname, position):
        backend.insert(fname, lname, position)
        clearFields()
        viewAllCommand()
        updateStatusText('Record created: {} {}'.format(fname, lname))
    else:
        updateStatusText('Record creation incomplete. Fill required fields.')

def deleteCommand():
    deleteID = formatter.reverseFormat(selectedRow)[0]
    backend.delete(deleteID)
    clearFields()
    viewAllCommand()
    updateStatusText(f'Record with ID {deleteID} deleted.')


def updateCommand():
    try:
        iden = formatter.reverseFormat(selectedRow)[0]
        fname, lname, position = fnameText.get(), lnameText.get(), positionText.get()
        backend.update(iden, fname, lname, position)
        clearFields()
        viewAllCommand()
        updateStatusText(f'Record with ID {iden} has been updated.')
    # if there is no selectedRow
    except NameError:
        updateStatusText('Please select a record to update.')


# Creating the Window
window = Tk()
window.geometry('700x380')
window.title('Tkinter/SQL GUI')
window.bind('<Return>', searchByEnter)
window.bind('<MouseWheel>', onMouseWheel)

# General styling constants
FAMILY = 'Helvetica'
WEIGHT = 'bold'

# Labels
PADX, PADY, LABELWIDTH = 15, 8, 15
LABELFONT = font.Font(family=FAMILY, size=10, weight=WEIGHT)
employeeCRUDLabel = Label(window, text='Created by: Dennis Mamrenko', pady=10, font=LABELFONT)
fnameLabel = Label(window, text='First Name:', padx=PADX, pady=PADY, width=LABELWIDTH, font=LABELFONT)
lnameLabel = Label(window, text='Last Name:', padx=PADX, pady=PADY, width=LABELWIDTH,  font=LABELFONT)
positionLabel = Label(window, text='Position:', padx=PADX, pady=PADY, width=LABELWIDTH,  font=LABELFONT)
idLabel = Label(window, text='ID:', padx=PADX, pady=PADY, width=LABELWIDTH,  font=LABELFONT)
resultsLabel = Label(window, text='Results:', font=LABELFONT)
statusLabel = Label(window, text='Status:', font=LABELFONT)

# Entries and associated StringVars
ENTRYWIDTH = 35
ENTRYFONT = font.Font(family=FAMILY, size=10, weight=WEIGHT)
fnameText = StringVar()
lnameText = StringVar()
positionText = StringVar()
idText = StringVar()
fnameEntry = Entry(window, width=ENTRYWIDTH, textvariable=fnameText, font=ENTRYFONT)
lnameEntry = Entry(window, width=ENTRYWIDTH, textvariable=lnameText, font=ENTRYFONT)
positionEntry = Entry(window, width=ENTRYWIDTH, textvariable=positionText, font=ENTRYFONT)
idEntry = Entry(window, width=ENTRYWIDTH, textvariable=idText, font=ENTRYFONT)

# Buttons
BUTTONWIDTH = 10
GREEN = '#2f963f'
RED = '#cc352d'
GREY = '#8b9194'
FOREGROUND = 'white'
BUTTONFONT = font.Font(family=FAMILY, size=12, weight=WEIGHT)
searchButton = Button(window, text='Search', width=BUTTONWIDTH, command=searchCommand, bg=GREEN, fg=FOREGROUND, font=BUTTONFONT)
createButton = Button(window, text='Create', width=BUTTONWIDTH, command=insertCommand, bg=GREEN, fg=FOREGROUND, font=BUTTONFONT)
clearButton = Button(window, text='Clear Fields', width=BUTTONWIDTH, command=clearFields, bg=GREY, fg=FOREGROUND, font=BUTTONFONT)
viewAllButton = Button(window, text='View All', width=BUTTONWIDTH, command=viewAllCommand, bg=GREY, fg=FOREGROUND, font=BUTTONFONT)
hideAllButton = Button(window, text='Hide All', width=BUTTONWIDTH, command=hideAllCommand, bg=GREY, fg=FOREGROUND, font=BUTTONFONT)
updateButton = Button(window, text='Update', width=BUTTONWIDTH, command=updateCommand, bg=RED, fg=FOREGROUND, font=BUTTONFONT)
deleteButton = Button(window, text='Delete', width=BUTTONWIDTH, command=deleteCommand, bg=RED, fg=FOREGROUND, font=BUTTONFONT)
# (CheckButtons)
strictValue = IntVar()
strictSearchButton = Checkbutton(window, text='Strict Search', variable=strictValue, onvalue=1, offvalue=0, font=LABELFONT)

# Listbox and Scrollbar
LISTBOXWIDTH = 60
LISTBOXITEMFONT = font.Font(family=FAMILY, size=8, weight=WEIGHT)
listboxFrame = Frame(window)
resultsScrollbar = Scrollbar(listboxFrame)
resultsListbox = Listbox(listboxFrame, width=LISTBOXWIDTH, yscrollcommand=resultsScrollbar.set, font=LISTBOXITEMFONT)
resultsListbox.bind('<<ListboxSelect>>', getSelectedRow)
resultsScrollbar.config(command = resultsListbox.yview)
resultsListbox.pack(side=LEFT, fill=X)
resultsScrollbar.pack(side=RIGHT, fill=Y)

# Validation Text
statusText = Text(window, width=20, height=9, wrap=WORD, font=LABELFONT)

# Placing Widgets
    # Labels
employeeCRUDLabel.grid(row=0, column=1, columnspan=2)
fnameLabel.grid(row=1, column=0, sticky=E)
lnameLabel.grid(row=2, column=0, sticky=E)
positionLabel.grid(row=3, column=0, sticky=E)
idLabel.grid(row=4, column=0, sticky=E)
resultsLabel.grid(row=5, column=1, columnspan=2)
statusLabel.grid(row=5, column=3)
    # Entries
fnameEntry.grid(row=1, column=1)
lnameEntry.grid(row=2, column=1)
positionEntry.grid(row=3, column=1)
idEntry.grid(row=4, column=1)
    # Buttons (and Checkbutton)
searchButton.grid(row=1, column=2)
strictSearchButton.grid(row=1, column=3)
createButton.grid(row=2, column=2)
clearButton.grid(row=3, column=2)
viewAllButton.grid(row=6, column=0)
hideAllButton.grid(row=7, column=0)
updateButton.grid(row=8, column=0)
deleteButton.grid(row=9, column=0)
    # Listbox and Scrollbar
listboxFrame.grid(row=6, column=1, columnspan=2, rowspan=4)
    # StatusText
statusText.grid(row=6, column=3, rowspan=4)

# Keeping the application running until close
window.mainloop()