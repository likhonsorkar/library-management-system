from rest_framework.viewsets import ModelViewSet
from books.models import Book, Category, Author
from books.serializers import BookSerializers, CategorySerializers, AuthorSerializers
from api.permissions import IsAdminOrReadOnly
# Create your views here.
class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    