from rest_framework import generics, permissions, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, ordering, and searching
    filter_backends = [rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # fields to filter
    ordering_fields = ['title', 'author', 'publication_year']   # fields to order by
    search_fields = ['title', 'author']                         # fields to search

class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # ...

class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    # ...

class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    # ...

class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    # ...

