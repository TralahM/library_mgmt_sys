from django.views.generic import ListView
from django.db.models import Q

from books.models import IssuedBook


class IssuedBookListView(ListView):
    model = IssuedBook
    template_name = "issued_book/issued_book_list.html"

    def get_queryset(self, *args, **kwargs):
        """Return appropriate queryset."""
        if not self.request.GET.get("q"):
            return IssuedBook.objects.all()
        return IssuedBook.objects.filter((Q(book_id__icontains=self.request.GET.get("q"))))
