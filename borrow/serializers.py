from borrow.models import BorrowRecord
from rest_framework import serializers

class BorrowRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book', 'member', 'borrow_date', 'return_date', 'due_date']
        read_only_fields = ['borrow_date', 'return_date', 'member']
class ReturnRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book', 'member', 'borrow_date', 'return_date', 'due_date']
        read_only_fields = ['book', 'member', 'borrow_date', 'due_date']

