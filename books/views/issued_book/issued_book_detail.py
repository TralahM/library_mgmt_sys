from django.views.generic import DetailView

from books.models import IssuedBook


class IssuedBookDetailView(DetailView):
    model = IssuedBook
    template_name = "issued_book/issued_book_detail.html"
