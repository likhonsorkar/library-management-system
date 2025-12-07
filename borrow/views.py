from rest_framework.viewsets import ModelViewSet
from borrow.models import BorrowRecord
from borrow.serializers import BorrowRecordSerializers

class BorrowRecordViewSet(ModelViewSet):
    serializer_class = BorrowRecordSerializers
    def get_queryset(self):
        if self.request.query_params.get('active') == 'true':
            return BorrowRecord.objects.filter(return_date__isnull=True)
        return BorrowRecord.objects.all()