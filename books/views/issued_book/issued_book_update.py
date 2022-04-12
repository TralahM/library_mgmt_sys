from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from books.models import IssuedBook

class IssuedBookUpdateView(UpdateView):
    model = IssuedBook
    fields = '__all__'
    template_name = "issued_book/issued_book_update.html"
    success_url = reverse_lazy('issued_book_list')
