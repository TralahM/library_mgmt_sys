from django.views.generic import ListView

from books.models import IssuedBook

class IssuedBookListView(ListView):
    model = IssuedBook
    template_name = "issued_book/issued_book_list.html"
