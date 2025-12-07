from django.db import models
from books.models import Book
from members.models import Member
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="loans")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return f"Loan of {self.book.title} to {self.member.email}"