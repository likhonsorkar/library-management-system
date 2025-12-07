from borrow.models import BorrowRecord
from rest_framework import serializers

class BorrowRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['book', 'member', 'borrow_date', 'return_date', 'due_date']