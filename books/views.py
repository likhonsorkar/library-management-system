from rest_framework.viewsets import ModelViewSet
from books.models import Book, Category, Author
from books.serializers import BookSerializers, CategorySerializers, AuthorSerializers
from books.permissions import IsLibrarianOrReadOnly
# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsLibrarianOrReadOnly]
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsLibrarianOrReadOnly]
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [IsLibrarianOrReadOnly]

    