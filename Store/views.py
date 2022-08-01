from django.shortcuts import render
from django.views import generic
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin



class BookListView(generic.ListView):

    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'book_list'



class BookDetailView(LoginRequiredMixin,generic.DetailView):

    model = Book
    template_name = 'store/book_detail.html'
    context_object_name = 'book_detail'
    login_url = 'account_login'


