import sqlite3

#Connect to/create database
conn = sqlite3.connect('data/biodynamic.db')
cur = conn.cursor()

#Create table if not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS biodynamic_calendar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        TIME TEXT NOT NULL,
        type TEXT NOT NULL
    )
''')

#Delete all records for testing
cur.execute('DELETE FROM biodynamic_calendar')

#Insert sample data
cur.execute('''
    INSERT INTO biodynamic_calendar (date,time,type)
    VALUES (?, ?, ?)
''', ('2025-07-04', '5:32AM', 'Leaf'))

conn.commit()

#Query data
cur.execute('SELECT * FROM biodynamic_calendar')
print(cur.fetchall())

conn.close()