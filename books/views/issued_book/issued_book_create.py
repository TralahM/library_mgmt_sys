from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from books.models import IssuedBook

class IssuedBookCreateView(CreateView):
    model = IssuedBook
    fields = '__all__'
    template_name = "issued_book/issued_book_create.html"
    success_url = reverse_lazy('issued_book_list')
