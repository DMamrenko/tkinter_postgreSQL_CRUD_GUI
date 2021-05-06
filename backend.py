import sqlite3
#using sqlite3 for testing purposes before moving along to postgreSQL

# Connect
def connect():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, first_name text, last_name text, position text)')
    conn.commit()
    conn.close()

# Searches
def looseSearch(iden='', fname='', lname='', position=''):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee WHERE id=? OR first_name=? OR last_name=? OR position=?', (iden, fname, lname, position))
    rows = cur.fetchall()
    conn.close()
    return rows

def strictSearch(iden=None, fname=None, lname=None, position=None):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM employee WHERE id=? OR first_name=? OR last_name=? OR position=?""", (iden, fname, lname, position))
    rows = cur.fetchall()
    conn.close()
    return rows

def idExists(iden):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee WHERE id=?', (iden))
    rows = cur.fetchall()
    conn.close()
    return len(rows) == 1

# Create
def insert(fname, lname, position):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO employee VALUES (NULL, ?, ?, ?)', (fname, lname, position))
    conn.commit()
    conn.close()

# Update
def update(iden, fname, lname, position):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('UPDATE employee SET first_name=?, last_name=?, position=? WHERE id=?', (fname, lname, position, iden))
    conn.commit()
    conn.close()

# Delete
def delete(iden):
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM employee WHERE id=?', (iden,))
    conn.commit()
    conn.close()

# View All
def viewAll():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    conn.close()
    return rows

# Extra functions
def clearDB():
    rows = viewAll()
    for record in rows:
        delete(record[0])

def displayAll():
    rows = viewAll()
    print('Results:')
    print(*rows, sep='\n')
    print('---------------------------------------')

def displayResults(results):
    print('Results:')
    print(*results, sep='\n')
    print('---------------------------------------')

def populateDB():
    insert('Abigail', 'Schrumpf', 'Physical Therapist')
    insert('Devin', 'Adkins', 'Software Developer')
    insert('Jeff', 'Payne', 'Database Manager')
    insert('Jack', 'Wallis', 'Athletic Monster')
    insert('Dennis', 'Mamrenko', 'Software Developer')
    insert('Vadim', 'Mamrenko', 'Mechanical Engineer')
    insert('Brooke', 'Mamrenko', 'Educator')
    insert('Ken', 'Schrumpf', 'Human Resources Director')
    insert('Daniel', 'Bones', 'Forklift Operator')
    insert('Allison', 'Orange', 'Logistics Manager')

def main():
    connect()

if __name__ == '__main__':
    main()