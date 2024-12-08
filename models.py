import sqlite3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def get_db_connection():
        # Helper method to establish a connection to the database
        conn = sqlite3.connect('library.db')
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn

    @staticmethod
    def add_book(title, author):
        conn = Book.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return {"id": book_id, "title": title, "author": author}

    @staticmethod
    def get_all_books(search_title=None, search_author=None):
        conn = Book.get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM books"
        params = []
        
        if search_title and search_author:
            query += " WHERE title LIKE ? AND author LIKE ?"
            params.extend([f"%{search_title}%", f"%{search_author}%"])
        elif search_title:
            query += " WHERE title LIKE ?"
            params.append(f"%{search_title}%")
        elif search_author:
            query += " WHERE author LIKE ?"
            params.append(f"%{search_author}%")
        
        cursor.execute(query, tuple(params))
        books = cursor.fetchall()
        conn.close()

        return [{"id": book["id"], "title": book["title"], "author": book["author"]} for book in books]
