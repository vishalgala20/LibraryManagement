from flask import Flask, jsonify, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database helper function to connect
def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a book (POST method) - form submission
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')

    # Check if title and author are provided
    if not title or not author:
        return jsonify({"message": "Title and author are required"}), 400

    # Add the new book to the SQLite database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()

    # Redirect to the "View Books" page after adding the book
    return redirect(url_for('display_books'))


# Route to add multiple books (POST method) - JSON API
@app.route('/add_books', methods=['POST'])
def add_books():
    data = request.get_json()  # Get the JSON data from the request
    books = data.get("books", [])  # Extract books from the request data
    
    # Check if it's a single book or a list of books
    if isinstance(books, dict):
        # Single book format, extract title and author
        title = books.get("title")
        author = books.get("author")
        if not title or not author:
            return jsonify({"message": "Title and author are required for the book"}), 400

        # Insert the single book into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()
        conn.close()

        return jsonify({"message": "Book added successfully!", "book": {"title": title, "author": author}}), 201
    
    elif isinstance(books, list) and books:
        # Multiple books format
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert multiple books into the database
        cursor.executemany('INSERT INTO books (title, author) VALUES (?, ?)', 
                           [(book["title"], book["author"]) for book in books])
        conn.commit()
        conn.close()

        return jsonify({"message": "Books added successfully!"}), 201
    
    return jsonify({"message": "Invalid data format"}), 400

# Route to search for books (with filtering by title and author)
@app.route('/books')
def display_books():
    search_title = request.args.get('title')  # Get title filter from URL parameters
    search_author = request.args.get('author')  # Get author filter from URL parameters

    conn = get_db_connection()
    cursor = conn.cursor()

    # Modify SQL query based on search filters
    if search_title and search_author:
        cursor.execute('SELECT title, author FROM books WHERE title LIKE ? AND author LIKE ?', 
                       (f'%{search_title}%', f'%{search_author}%',))
    elif search_title:
        cursor.execute('SELECT title, author FROM books WHERE title LIKE ?', (f'%{search_title}%',))
    elif search_author:
        cursor.execute('SELECT title, author FROM books WHERE author LIKE ?', (f'%{search_author}%',))
    else:
        cursor.execute('SELECT title, author FROM books')

    books = cursor.fetchall()
    conn.close()

    return render_template('books.html', books=books, search_title=search_title, search_author=search_author)

# Route to render the Add Book page
@app.route('/add_books')
def add_books_page():
    return render_template('add_books.html')

if __name__ == '__main__':
    app.run(debug=True)
