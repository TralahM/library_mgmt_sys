from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
from django.shortcuts import render, redirect
from books.models import IssuedBook, Book


def before_login(request):
    """Show this before user chooses how to login."""
    if request.user.is_authenticated:
        if request.user.is_librarian:
            return redirect("after_login")
        else:
            return redirect(f"/student/detail/{request.user.student.pk}/")
    return render(request, "index.html")


@login_required
def after_login(request):
    """After login show appropriate home page."""
    Books = Book.objects.all()
    if request.user.utype == "STUDENT":
        borrowed_books = IssuedBook.objects.filter(student_id=request.user.id)
        return render(
            request,
            "student_profile.html",
            {
                "books": borrowed_books,
            },
        )
    else:
        # render librarian request.
        return render(
            request,
            "librarian_home.html",
            {
                "object_list": Books,
            },
        )
        ...
