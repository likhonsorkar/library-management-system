from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from borrow.models import BorrowRecord
from borrow.serializers import BorrowRecordSerializers, ReturnRecordSerializers
from api.permissions import IsAuthenticated, IsAdminOrReadOnly
from members.models import Member
from drf_yasg.utils import swagger_auto_schema

class BorrowRecordViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BorrowRecordSerializers
    def get_queryset(self):
        if self.request.query_params.get('active') == 'true':
            return BorrowRecord.objects.filter(return_date__isnull=True)
        return BorrowRecord.objects.all()
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
    @swagger_auto_schema(
        operation_summary="List Borrow Records",
        operation_description="Retrieve a list of book borrow records. Use the 'active' parameter to filter unreturned books.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="Create Borrow Record",
        operation_description="Log a new book borrowing. The system automatically assigns the record to the authenticated member.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="Partial Update Borrow Record",
        operation_description="Update specific fields of an existing borrow record.",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="Full Update Borrow Record",
        operation_description="Replace an entire borrow record entry with new data.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="Delete Borrow Record",
        operation_description="Permanently remove a borrow record from the system.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary="Get Borrow Record Details",
        operation_description="Retrieve full details of a specific borrow record by its ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
@swagger_auto_schema(
    operation_summary="Borrow Records Management (Admin)",
    operation_description="API for administrators to view and manage borrow records, including marking books as returned."
)
class ReturnRecordViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ReturnRecordSerializers
    def get_queryset(self):
        if self.request.query_params.get('active') == 'true':
            return BorrowRecord.objects.filter(return_date__isnull=True)
        return BorrowRecord.objects.all()

    @swagger_auto_schema(
        operation_summary="List Return Records",
        operation_description="Retrieve a list of all borrow/return records. Admin access only. 'active' parameter filters unreturned books."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get Return Record Details",
        operation_description="Retrieve details of a specific borrow/return record by ID. Admin access only."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Return Record",
        operation_description="Update an existing borrow record, typically to mark a book as returned. Admin access only."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)