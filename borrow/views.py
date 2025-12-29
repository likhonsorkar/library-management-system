from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from borrow.models import BorrowRecord
from borrow.serializers import BorrowRecordSerializers, ReturnRecordSerializers
from api.permissions import IsAuthenticated, IsAdminOrReadOnly
from members.models import Member

class BorrowRecordViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BorrowRecordSerializers
    def get_queryset(self):
        if self.request.query_params.get('active') == 'true':
            return BorrowRecord.objects.filter(return_date__isnull=True)
        return BorrowRecord.objects.all()
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
class ReturnRecordViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ReturnRecordSerializers
    def get_queryset(self):
        if self.request.query_params.get('active') == 'true':
            return BorrowRecord.objects.filter(return_date__isnull=True)
        return BorrowRecord.objects.all()

    