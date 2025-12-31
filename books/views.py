from rest_framework.viewsets import ModelViewSet
from books.models import Book, Category, Author
from books.serializers import BookSerializers, CategorySerializers, AuthorSerializers
from api.permissions import IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(
    operation_summary="Book Management",
    operation_description="API for managing books, including adding, updating, and retrieving book details. Admin access only for modifications."
)
class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    @swagger_auto_schema(
        operation_summary="List Books",
        operation_description="Retrieve a list of all books in the library."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create Book",
        operation_description="Add a new book to the library. Admin access required."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve Book",
        operation_description="Retrieve details of a specific book by its ID."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Book (Full)",
        operation_description="Fully update an existing book's details. Admin access required."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Book (Partial)",
        operation_description="Partially update an existing book's details. Admin access required."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Book",
        operation_description="Delete a book from the library. Admin access required."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    @swagger_auto_schema(
        operation_summary="List Categories",
        operation_description="Retrieve a list of all book categories."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create Category",
        operation_description="Add a new book category. Admin access required."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve Category",
        operation_description="Retrieve details of a specific book category by its ID."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Category (Full)",
        operation_description="Fully update an existing book category's details. Admin access required."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Category (Partial)",
        operation_description="Partially update an existing book category's details. Admin access required."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Category",
        operation_description="Delete a book category. Admin access required."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
@swagger_auto_schema(
    operation_summary="Author Management",
    operation_description="API for managing authors, including adding, updating, and retrieving author details. Admin access only for modifications."
)
class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    @swagger_auto_schema(
        operation_summary="List Authors",
        operation_description="Retrieve a list of all authors."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create Author",
        operation_description="Add a new author. Admin access required."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve Author",
        operation_description="Retrieve details of a specific author by their ID."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Author (Full)",
        operation_description="Fully update an existing author's details. Admin access required."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Author (Partial)",
        operation_description="Partially update an existing author's details. Admin access required."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Author",
        operation_description="Delete an author. Admin access required."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    