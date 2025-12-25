from rest_framework.viewsets import ModelViewSet
from books.models import Book, Category, Author
from books.serializers import BookSerializers, CategorySerializers, AuthorSerializers
from books.permissions import IsLibrarianOrReadOnly

class BookViewSet(ModelViewSet):
    """
    ViewSet for managing books.

    **Permissions:**
    - Authenticated users can view books (list and retrieve).
    - Only librarians (staff users) can create, update, or delete books.

    **Actions:**
    - `list`: Returns a list of all books.
    - `retrieve`: Returns the details of a specific book.
    - `create`: Creates a new book. (Librarian only)
    - `update`: Updates an existing book. (Librarian only)
    - `partial_update`: Partially updates an existing book. (Librarian only)
    - `destroy`: Deletes a book. (Librarian only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsLibrarianOrReadOnly]

class CategoryViewSet(ModelViewSet):
    """
    ViewSet for managing book categories.

    **Permissions:**
    - Authenticated users can view categories.
    - Only librarians can create, update, or delete categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsLibrarianOrReadOnly]

class AuthorViewSet(ModelViewSet):
    """
    ViewSet for managing authors.

    **Permissions:**
    - Authenticated users can view authors.
    - Only librarians can create, update, or delete authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [IsLibrarianOrReadOnly]