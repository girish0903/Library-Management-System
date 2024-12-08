import unittest
import json
from app import app

class LibraryAPIUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Library Management System API!", response.get_data(as_text=True))

    def test_create_book(self):
        response = self.app.post('/books', data=json.dumps({
            "title": "Book Title",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Book Title")
        self.assertEqual(data["author"], "Author Name")
        self.assertEqual(data["year_published"], 2021)

    def test_read_books(self):
        self.app.post('/books', data=json.dumps({
            "title": "Book Title",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')

        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertGreater(len(data), 0)

    def test_update_book(self):
        response = self.app.post('/books', data=json.dumps({
            "title": "Book Title",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')

        book_id = json.loads(response.get_data(as_text=True))['id']
        
        response = self.app.put(f'/books/{book_id}', data=json.dumps({
            "title": "Updated Book Title",
            "author": "Updated Author Name",
            "year_published": 2022
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["title"], "Updated Book Title")
        self.assertEqual(data["author"], "Updated Author Name")
        self.assertEqual(data["year_published"], 2022)

    def test_delete_book(self):
        response = self.app.post('/books', data=json.dumps({
            "title": "Book Title",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')

        book_id = json.loads(response.get_data(as_text=True))['id']
        
        response = self.app.delete(f'/books/{book_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["message"], "Book deleted")

    def test_search_books(self):
        self.app.post('/books', data=json.dumps({
            "title": "Book Title",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')

        response = self.app.get('/books/search?title=Book')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertGreater(len(data), 0)

    def test_pagination(self):
        for i in range(15):
            self.app.post('/books', data=json.dumps({
                "title": f"Book {i}",
                "author": "Author Name",
                "year_published": 2021
            }), content_type='application/json')

        response = self.app.get('/books/pagination?page=1&per_page=10')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 10)

    def test_invalid_update(self):
        response = self.app.put('/books/999', data=json.dumps({
            "title": "Non-existent Book",
            "author": "Author Name",
            "year_published": 2021
        }), content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["error"], "Book not found")

if __name__ == '__main__':
    unittest.main()
