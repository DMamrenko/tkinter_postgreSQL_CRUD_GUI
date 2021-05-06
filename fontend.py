"""
A CRUD program for records of employees.
"""
from tkinter import *
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

def getSelectedRow(event):
    try:
        global selectedRow
        i = resultsListbox.curselection()[0]
        selectedRow = resultsListbox.get(i)
        populateFieldsFromSelectedRow()
    except IndexError:
        pass

def populateFieldsFromSelectedRow():
    # print(selectedRow)
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

def hideAllCommand():
    clearResultsListbox()

def searchCommand():
    clearResultsListbox()
    rows = backend.looseSearch(idText.get(), fnameText.get(), lnameText.get(), positionText.get())
    searchResults = formatter.formatResults(rows)
    for row in searchResults:
        resultsListbox.insert(END, row)
    updateStatusText('Displaying search results.')

def insertCommand():
    if validator.validateInsertion(fnameText.get(), lnameText.get(), positionText.get()):
        backend.insert(fnameText.get(), lnameText.get(), positionText.get())
        updateStatusText('Record created.')
        clearFields()
    else:
        print('Invalid Insertion')

def deleteCommand():
    deleteID = formatter.reverseFormat(selectedRow)[0]
    backend.delete(deleteID)
    clearResultsListbox()
    viewAllCommand()
    updateStatusText(f'Record with ID {iden} deleted.')
    clearFields()

def updateCommand():
    iden= formatter.reverseFormat(selectedRow)[0]
    backend.update(iden, fnameText.get(), lnameText.get(), positionText.get())
    clearResultsListbox()
    viewAllCommand()
    updateStatusText(f'Record with ID {iden} has been updated.')
    clearFields()

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

# Entries and associated StringVars
ENTRYWIDTH = 35
fnameText = StringVar()
lnameText = StringVar()
positionText = StringVar()
idText = StringVar()
fnameEntry = Entry(window, width=ENTRYWIDTH, textvariable=fnameText)
lnameEntry = Entry(window, width=ENTRYWIDTH, textvariable=lnameText)
positionEntry = Entry(window, width=ENTRYWIDTH, textvariable=positionText)
idEntry = Entry(window, width=ENTRYWIDTH, textvariable=idText)

# Buttons
BUTTONWIDTH = 10
searchButton = Button(window, text='Search', width=BUTTONWIDTH, command=searchCommand)
createButton = Button(window, text='Create', width=BUTTONWIDTH, command=insertCommand)
clearButton = Button(window, text='Clear Fields', width=BUTTONWIDTH, command=clearFields)
viewAllButton = Button(window, text='View All', width=BUTTONWIDTH, command=viewAllCommand)
hideAllButton = Button(window, text='Hide All', width=BUTTONWIDTH, command=hideAllCommand)
updateButton = Button(window, text='Update', width=BUTTONWIDTH, command=updateCommand)
deleteButton = Button(window, text='Delete', width=BUTTONWIDTH, command=deleteCommand)
# (CheckButtons)
strictValue = IntVar()
strictSearchButton = Checkbutton(window, text='Strict Search', variable=strictValue, onvalue=1, offvalue=0)

# Listbox and Scrollbar
LISTBOXWIDTH = 60
listboxFrame = Frame(window)
resultsScrollbar = Scrollbar(listboxFrame)
resultsListbox = Listbox(listboxFrame, width=LISTBOXWIDTH, yscrollcommand=resultsScrollbar)
resultsListbox.bind('<<ListboxSelect>>', getSelectedRow)
resultsScrollbar.config(command = resultsListbox.yview)
resultsListbox.pack(side=LEFT, fill=X)
resultsScrollbar.pack(side=RIGHT, fill=Y)

# Validation Text
statusText = Text(window, width=10, height=8, wrap=WORD)

# Placing Widgets
    # Labels
employeeCRUDLabel.grid(row=0, column=1)
fnameLabel.grid(row=1, column=0, sticky=E)
lnameLabel.grid(row=2, column=0, sticky=E)
positionLabel.grid(row=3, column=0, sticky=E)
idLabel.grid(row=4, column=0, sticky=E)
resultsLabel.grid(row=5, column=1)
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