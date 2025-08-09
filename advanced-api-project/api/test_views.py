from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.author = Author.objects.create(name='Jane Doe')
        self.book = Book.objects.create(title='Test Book', publication_year=2000, author=self.author)

    def test_list_books(self):
        url = reverse('book-list-create')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(resp.data, list))

    def test_create_book_requires_auth(self):
        url = reverse('book-list-create')
        data = {'title': 'New Book', 'publication_year': 2020, 'author': self.author.id}
        resp = self.client.post(url, data, format='json')
        # Should be forbidden because unauthenticated (we used IsAuthenticated for writes)
        self.assertIn(resp.status_code, (status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))

        # Authenticate and try again
        self.client.login(username='tester', password='pass1234')
        resp2 = self.client.post(url, data, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)

    def test_retrieve_update_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        # Retrieve
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Update requires auth
        data = {'title': 'Updated Title', 'publication_year': 2001, 'author': self.author.id}
        resp2 = self.client.put(url, data, format='json')
        self.assertIn(resp2.status_code, (status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))
        # Authenticate and update
        self.client.login(username='tester', password='pass1234')
        resp3 = self.client.put(url, data, format='json')
        self.assertEqual(resp3.status_code, status.HTTP_200_OK)
        # Delete
        resp4 = self.client.delete(url)
        self.assertEqual(resp4.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_search_order(self):
        # Create extra books
        author2 = Author.objects.create(name='John Smith')
        Book.objects.create(title='Another', publication_year=2010, author=author2)
        url = reverse('book-list-create')
        # Filter by publication_year
        resp = self.client.get(url + '?publication_year=2010')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Search by title
        resp2 = self.client.get(url + '?search=Another')
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        # Order by -publication_year
        resp3 = self.client.get(url + '?ordering=-publication_year')
        self.assertEqual(resp3.status_code, status.HTTP_200_OK)
