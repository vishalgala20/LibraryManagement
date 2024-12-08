import pytest
import json
from app import app

@pytest.fixture
def client():
    # Create a test client for making requests to the Flask app
    with app.test_client() as client:
        yield client

def test_add_book(client):
    # Test the POST method to add a book
    response = client.post('/books', 
                           data=json.dumps({"title": "Test Book", "author": "Test Author"}), 
                           content_type='application/json')
    
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["message"] == "Book added successfully!"
    assert data["book"]["title"] == "Test Book"
    assert data["book"]["author"] == "Test Author"

def test_get_books(client):
    # Test the GET method to retrieve books
    client.post('/books', data=json.dumps({"title": "Book 1", "author": "Author 1"}), content_type='application/json')
    client.post('/books', data=json.dumps({"title": "Book 2", "author": "Author 2"}), content_type='application/json')
    
    response = client.get('/books')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(data) >= 2  # We added two books

def test_search_books_by_title(client):
    # Test search functionality by title
    client.post('/books', data=json.dumps({"title": "Search Book", "author": "Search Author"}), content_type='application/json')
    
    response = client.get('/books?title=Search Book')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "Search Book"
    assert data[0]["author"] == "Search Author"

def test_search_books_by_author(client):
    # Test search functionality by author
    client.post('/books', data=json.dumps({"title": "Another Book", "author": "Another Author"}), content_type='application/json')
    
    response = client.get('/books?author=Another Author')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["author"] == "Another Author"

def test_invalid_data(client):
    # Test the case where missing title or author returns an error
    response = client.post('/books', 
                           data=json.dumps({"title": "", "author": ""}), 
                           content_type='application/json')
    
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["message"] == "Title and Author are required"
