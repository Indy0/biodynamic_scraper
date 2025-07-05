import sqlite3

def save_to_db(scraped_data):
    conn = sqlite3.connect('data/biodynamic.db')
    cur = conn.cursor()

    #Create table if doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS biodynamic_calendar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            type TEXT NOT NULL,
            UNIQUE(date, time, type)
        )
    ''')

    for date, events in scraped_data.items():
            for event in events:
                  cur.execute('''
                    INSERT OR IGNORE INTO biodynamic_calendar (date, time, type)
                    VALUES (?, ?, ?)
                ''', (date, event['time'], event['state']))
                  
    conn.commit()
    conn.close()