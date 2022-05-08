from django.shortcuts import render
from django.views.generic import ListView

from .models import Module, Book


class ModuleListView(ListView):
    model = Module

    template_name = 'main.html'


def more_about_module(request, pk):
    module = Module.objects.get(id=pk)
    books = module.books.all()

    return render(request, 'about.html', {
        "module": module,
        "books": books
    })


def more_about_book(request, pk):
    book = Book.objects.get(id=pk)

    return render(request, 'book.html', {
        "book": book
    })

# end
# Created: https://github.com/alwayswanna
