from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from borrow.models import BorrowRecord
from borrow.serializers import BorrowRecordSerializers

class BorrowRecordViewSet(ModelViewSet):
    serializer_class = BorrowRecordSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = BorrowRecord.objects.all()
        else:
            queryset = BorrowRecord.objects.filter(member=user)
        if self.request.query_params.get('active') == 'true':
            return queryset.filter(return_date__isnull=True)
        return queryset