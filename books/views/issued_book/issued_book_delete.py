from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from books.models import IssuedBook

class IssuedBookDeleteView(DeleteView):
    model = IssuedBook
    template_name = "issued_book/issued_book_delete.html"
    success_url = reverse_lazy('issued_book_list')