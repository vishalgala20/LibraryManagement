import sqlite3

# Connect to SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create a table for storing books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
