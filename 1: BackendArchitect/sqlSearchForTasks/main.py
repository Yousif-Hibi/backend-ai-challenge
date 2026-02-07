import sqlite3

try:
    with sqlite3.connect('Task_App.db') as conn:
        cur = conn.cursor()
        query = """
            SELECT title 
            FROM tasks 
            WHERE users_id = 1 
            AND is_completed = 0
            """
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
except sqlite3.OperationalError as e:
    print(e)