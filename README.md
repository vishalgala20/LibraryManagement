Library Management System

Project Title:
A simple web-based library management system for managing books in a library.

Description:
This project is a basic implementation of a library management system using Flask and SQLite. It allows users to view, add, and filter books in the library. The system stores the book information (title and author) in an SQLite database and provides a user-friendly interface to interact with the library catalog.

---

Getting Started

Dependencies:
- Python 3.x
- Flask
- SQLite3 (SQLite comes pre-installed with Python)
- HTML, CSS, JavaScript for the front-end

Installing:

1. Clone the repository:
   To download the project to your local machine, use the following command:

   git clone https://github.com/your-username/LibraryManagement.git

2. Navigate to the project directory:
   
   cd LibraryManagement

3. Install the required Python dependencies:
   If you don't already have Flask installed, use the following command to install it:

   pip install flask

4. Database Setup:
   The database `library.db` will be automatically created when the app is run for the first time, so there's no need for any initial setup.

---

Executing the Program:

1. Run the Flask application:
   To start the server and run the application locally, execute the following command:

   python app.py

2. Access the application:
   After running the application, you can access it in your browser at the following URL:

   http://127.0.0.1:5000/

3. Add, View, and Filter Books:
   - Add new books via the "Add New Book" button.
   - View all books and filter them by title or author.

---

Help:

- If you run into issues with the program not starting, make sure you have Python 3.x installed and that Flask is properly installed.
- If you encounter issues accessing the database, ensure that the `library.db` file exists in the project directory.

Command to run if program contains helper info:
If you need to run any helper info or debug the project, use the following command to check for issues:

flask --help

---

Authors:

- Dominique Pizzie (initial project, contact via GitHub)

---

Version History:

- 0.2 - Various bug fixes and optimizations
- 0.1 - Initial Release

---

License:

This project is licensed under the [MIT License] (LICENSE.md) - see the LICENSE.md file for details.

---

Acknowledgments:

- Inspiration from various open-source projects
- Code snippets and tips from Stack Overflow
