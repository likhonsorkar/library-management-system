from rest_framework.viewsets import ModelViewSet
from books.models import Book, Category, Author
from books.serializers import BookSerializers, CategorySerializers, AuthorSerializers
# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    