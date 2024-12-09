import sqlite3

# Connect to the existing SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Add the borrowed column if it doesn't already exist
try:
    cursor.execute('''
    ALTER TABLE books ADD COLUMN borrowed INTEGER DEFAULT 0
    ''')
    print("Column 'borrowed' added successfully!")
except sqlite3.OperationalError as e:
    print("Error:", e)

# Commit the changes and close the connection
conn.commit()
conn.close()
