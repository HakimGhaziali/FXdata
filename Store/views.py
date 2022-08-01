from django.shortcuts import render
from django.views import generic
from .models import Book




class BookListView(generic.ListView):

    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'book_list'



class BookDetailView(generic.DetailView):

    model = Book
    template_name = 'store/book_detail.html'
    context_object_name = 'book_detail'


