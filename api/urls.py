from django.urls import path, include
from books.views import BookViewSet, CategoryViewSet, AuthorViewSet
from members.views import MemberViewSet
from borrow.views import BorrowRecordViewSet, ReturnRecordViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename="books")
router.register('categories', CategoryViewSet, basename="categories")
router.register('authors', AuthorViewSet, basename="authors")
# router.register('members', MemberViewSet, basename='members')
router.register('borrow-records', BorrowRecordViewSet, basename='borrow-records')
router.register('return-records', ReturnRecordViewSet, basename='return-records')
urlpatterns = [
    path('', include(router.urls))
]
