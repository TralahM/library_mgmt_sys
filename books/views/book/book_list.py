from django.views.generic import ListView
from django.db.models import Q
from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"

    def get_queryset(self, *args, **kwargs):
        """Return appropriate queryset."""
        # print(self.request.GET)
        if not self.request.GET.get("q"):
            return Book.objects.all()
        else:
            return Book.objects.filter(
                (
                    Q(name__icontains=self.request.GET.get("q"))
                    | Q(author__icontains=self.request.GET.get("q"))
                )
            )
