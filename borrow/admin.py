from django.contrib import admin
from borrow.models import BorrowRecord

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'due_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'member__email')
    readonly_fields = ('borrow_date',)
    fieldsets = (
        (None, {
            'fields': ('book', 'member')
        }),
        ('Dates', {
            'fields': ('borrow_date', 'due_date', 'return_date')
        }),
    )