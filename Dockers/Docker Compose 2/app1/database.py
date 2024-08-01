import sqlite3

conn = sqlite3.connect('/data/database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS persons
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')

conn.commit()
conn.close()
