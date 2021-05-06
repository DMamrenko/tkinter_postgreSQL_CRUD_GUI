def formatResults(rows):
    displayRows = []
    for (iden, fname, lname, position) in rows:
        displayRows.append(f'{iden} {lname}, {fname} - {position}')
    return displayRows

# Displayed row will be selected, we want to extract the data from it
def reverseFormat(displayed):
    idLF, position = displayed.split(' - ')
    idL, F = idLF.split(', ')
    iden, L = idL.split()
    return([iden, F, L, position])
