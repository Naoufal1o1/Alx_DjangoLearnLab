from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(title='Book 1', author='Author 1', publication_year=2020)

    def test_authenticated_book_create(self):
        self.client.login(username='testuser', password='testpass')

        url = '/api/books/create/'
        data = {'title': 'New Book', 'author': 'John Doe', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
