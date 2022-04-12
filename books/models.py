from django.db import models
from datetime import datetime, timedelta


class Department(models.Model):
    """DepartMent."""

    name = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        """Return string repr."""
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    department = models.ForeignKey(
        to="books.Department",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        default=2000.00,
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return str(self.name) + " [" + str(self.isbn) + "]"


def expiry(days=14):
    """Return 14 day expiry."""
    return datetime.today() + timedelta(days=days)


class IssuedBook(models.Model):
    """An Issued Book."""

    student = models.ForeignKey(
        to="user_accounts.Student",
        on_delete=models.CASCADE,
        to_field="library_card_number",
        related_name="borrowed_books",
    )
    book = models.ForeignKey(to="books.Book", on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=expiry)
    return_date = models.DateField(null=True, blank=True)
    is_lost = models.BooleanField(default=False)
