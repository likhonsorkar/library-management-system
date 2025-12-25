from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from borrow.models import BorrowRecord
from borrow.serializers import BorrowRecordSerializers

class BorrowRecordViewSet(ModelViewSet):
    """
    ViewSet for managing borrow records.
    **Permissions:**
    - Any authenticated user can create, view, and manage their own borrow records.
    - Librarians can view all borrow records.
    **Queryset Filtering:**
    - If the user is a librarian, the queryset includes all borrow records.
    - If the user is a member, the queryset is filtered to only include their own borrow records.
    - The `?active=true` query parameter can be used to filter for active borrow records (where `return_date` is null).
    """
    serializer_class = BorrowRecordSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return BorrowRecord.objects.none()
        user = self.request.user
        if user.is_staff:
            queryset = BorrowRecord.objects.all()
        else:
            queryset = BorrowRecord.objects.filter(member=user)
        
        if self.request.query_params.get('active') == 'true':
            return queryset.filter(return_date__isnull=True)
        return queryset