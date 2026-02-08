import sqlite3

sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL
        );""",
    """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            title TEXT NOT NULL, 
            users_id INTEGER NOT NULL, 
            due_date DATE NOT NULL, 
            is_completed BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (users_id) REFERENCES users (id)
        );"""
]

# Data to insert
users_data = [('Alice',), ('Bob',), ('Charlie',)]

tasks_data = [
    ('Setup workspace', 1, '2026-02-10', 1),
    ('Buy coffee beans', 1, '2026-02-5', 0),
    ('Refactor API', 1, '2026-02-15', 0),
    ('Update documentation', 1, '2026-02-6', 0),
    ('Fix CSS bugs', 2, '2026-02-12', 1),
    ('Email client', 2, '2026-02-2', 0),
    ('Weekly backup', 2, '2026-02-1', 0),
    ('Gym session', 3, '2026-02-08', 0),
    ('Read SQL book', 3, '2026-02-09', 1),
    ('Submit report', 3, '2026-02-1', 0)
]

try:
    with sqlite3.connect('Task_App.db') as conn:
        cursor = conn.cursor()
        
        # 1. Create Tables
        for statement in sql_statements:
            cursor.execute(statement)

        # 2. Enable Foreign Keys (Crucial for the link to work!)
        cursor.execute("PRAGMA foreign_keys = ON;")

        # 3. Insert Users
        cursor.executemany("INSERT INTO users (name) VALUES (?);", users_data)
        
        # 4. Insert Tasks
        cursor.executemany("""
            INSERT INTO tasks (title, users_id, due_date, is_completed) 
            VALUES (?, ?, ?, ?);
        """, tasks_data)

        conn.commit()
        print("Database initialized with 3 users and 10 tasks.")

except sqlite3.Error as e:
    print("Database error:", e)