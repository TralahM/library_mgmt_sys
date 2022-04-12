from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from books.models import Book

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "book/book_update.html"
    success_url = reverse_lazy('book_list')
