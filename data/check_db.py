import sqlite3

def check_db():
    conn = sqlite3.connect('data/biodynamic.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM biodynamic_calendar ORDER BY date, time')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    check_db()
